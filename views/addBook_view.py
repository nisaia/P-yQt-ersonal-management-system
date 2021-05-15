import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QMainWindow, QDialog
from ui.addBook_window import *
from views.coverIllustration_view import *
from database.db import session
from database.models import *
from PyQt5.QtGui import QPixmap
from utils.custom_exceptions import NoInputException
from sqlalchemy.exc import IntegrityError
from utils.constants import COVER_PATH
from os.path import join
from PyQt5.QtCore import QUrl
import shutil
from utils.functions import openDialog

class AddBookView(QWidget):
    
    def __init__(self, parent):

        self.file_name = ""

        super().__init__(parent)
        self.ui = Ui_addBook_window()
        self.ui.setupUi(self)

        
        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.bookPreview_button.clicked.connect(self.displayCover)
                
        self.ui.addBook_button_1.clicked.connect(self.addBook)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def updateComboBox(self):
        self.ui.bookAuthor_comboBox.clear()
        self.ui.bookGenre_comboBox.clear()

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.bookAuthor_comboBox.addItem('No authors founded')
            self.ui.bookAuthor_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.bookAuthor_comboBox.addItem(str(author.name + " " + author.surname))
            self.ui.bookAuthor_comboBox.setDisabled(False)

        genres = session.query(Genre).all()
        if len(genres) == 0:
            self.ui.bookGenre_comboBox.addItem('No genres founded')
            self.ui.bookGenre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.bookGenre_comboBox.addItem(genre.name)
            self.ui.bookGenre_comboBox.setDisabled(False)

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        if len(file_name) != 0:
            self.ui.bookCoverPath_label.setText(file_name)
            self.ui.bookCoverPath_label.setVisible(True)
            self.ui.bookPreview_button.setVisible(True)

    def displayCover(self):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(self.ui.bookCoverPath_label.text())
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)
        coverIllustration_window.ui.coverIllustration_label.setScaledContents(True)

        coverIllustration_window.exec_()

    def addBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.bookIsbn_lineEdit.text()
            author = session.query(Author).filter_by(id=self.ui.bookAuthor_comboBox.currentIndex() + 1).first()
            genre = session.query(Genre).filter_by(id=self.ui.bookGenre_comboBox.currentIndex() + 1).first()
            cover_path = self.ui.bookCoverPath_label.text()


            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif genre == None: raise NoInputException('Enter the genre of the book')
            elif len(cover_path) == 0: raise NoInputException('Enter the cover image')

            file_name = QUrl.fromLocalFile(cover_path).fileName()
            new_cover_path = join(COVER_PATH, file_name)
            description = self.ui.bookDescription_plainTextEdit.toPlainText()

            book = Book(title=book_title,
                        isbn=isbn,
                        author_id=author.id,
                        genre_id=genre.id,
                        description=description,
                        cover_path=new_cover_path)
            
            session.add(book)
            session.commit()

            shutil.copy(cover_path, new_cover_path)

            #results = session.query(Book, Author, Category).select_from(Book).join(Author).join(Category).all()
            #print(session.query(Book).join(Book.category_id).join(Book.author_id)).all()
            #for book, author, category in results:
                #print(book.title, author.name, author.surname, category.name)

            self.clearAll()

            openDialog(QMessageBox.Information, 'Book added', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Book already inserted', 'Error')
            session.rollback()

    def clearAll(self):
        self.ui.bookTitle_lineEdit.clear()
        self.ui.bookIsbn_lineEdit.clear()
        self.ui.bookAuthor_comboBox.setCurrentIndex(0)
        self.ui.bookGenre_comboBox.setCurrentIndex(0)
        self.ui.bookCoverPath_label.setText("")
        self.ui.bookCoverPath_label.setVisible(False)
        self.ui.bookPreview_button.setVisible(False)
        self.ui.bookDescription_plainTextEdit.clear()
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
        self.ui.preview_button.clicked.connect(self.displayCover)
                
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        self.show()

    def updateComboBox(self):
        self.ui.author_comboBox.clear()
        self.ui.category_comboBox.clear()

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.author_comboBox.addItem('No authors founded')
            self.ui.author_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.author_comboBox.addItem(str(author.name + " " + author.surname))
            self.ui.author_comboBox.setDisabled(False)

        categories = session.query(Category).all()
        if len(categories) == 0:
            self.ui.category_comboBox.addItem('No categories founded')
            self.ui.category_comboBox.setDisabled(True)
        else:
            for category in categories:
                self.ui.category_comboBox.addItem(category.name)
            self.ui.category_comboBox.setDisabled(False)

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        if len(file_name) != 0:
            self.ui.coverPath_label.setText(file_name)
            self.ui.coverPath_label.setVisible(True)
            self.ui.preview_button.setVisible(True)

    def displayCover(self):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(self.ui.coverPath_label.text())
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)
        coverIllustration_window.ui.coverIllustration_label.setScaledContents(True)

        coverIllustration_window.exec_()

    def addBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.isbn_lineEdit.text()
            author = session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex() + 1).first()
            category = session.query(Category).filter_by(id=self.ui.category_comboBox.currentIndex() + 1).first()


            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif category == None: raise NoInputException('Enter the category of the book')

            old_cover_path = self.ui.coverPath_label.text()
            file_name = QUrl.fromLocalFile(old_cover_path).fileName()
            new_cover_path = join(COVER_PATH, file_name)
            description = self.ui.description_plainTextEdit.toPlainText()

            book = Book(title=book_title,
                        isbn=isbn,
                        author_id=author.id,
                        category_id=category.id,
                        description=description,
                        cover_path=new_cover_path)
            
            session.add(book)
            session.commit()

            shutil.copy(old_cover_path, new_cover_path)

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
        self.ui.isbn_lineEdit.clear()
        self.ui.author_comboBox.setCurrentIndex(0)
        self.ui.category_comboBox.setCurrentIndex(0)
        self.ui.coverPath_label.setText("")
        self.ui.coverPath_label.setVisible(False)
        self.ui.preview_button.setVisible(False)
        self.ui.description_plainTextEdit.clear()
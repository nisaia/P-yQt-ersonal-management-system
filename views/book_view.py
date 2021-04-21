import sys
from PyQt5.QtWidgets import QWidget
from ui.book_window import *
from PyQt5.QtGui import QPixmap
from database.models import *
from database.db import session
from utils.custom_exceptions import *
from sqlalchemy.exc import IntegrityError
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from views.coverIllustration_view import *


class BookView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_book_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.preview_button.clicked.connect(self.displayCover)

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        self.show()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        self.cover_path = file_name
        self.ui.coverPath_label.setText(self.cover_path)
        self.ui.coverPath_label.setVisible(True)
        self.ui.preview_button.setVisible(True)

    def displayCover(self):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(self.cover_path)
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)

        coverIllustration_window.exec_()

    def update(self):
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

    def setValue(self, book, author, category):
        self.book = book
        self.author = author
        self.category = category

        # FIRST TAB
        self.ui.title.setText(self.book.title)
        self.ui.isbn.setText(self.book.isbn)
        image = QPixmap(self.book.cover_path)
        image = image.scaled(self.ui.cover.width(), self.ui.cover.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.cover.setPixmap(image)
        self.ui.cover.setScaledContents(True)
        self.ui.author.setText(self.author.name + " " + self.author.surname)
        self.ui.category.setText(self.category.name)
        self.ui.description.setText(self.book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(self.book.title)
        self.ui.isbn_lineEdit.setText(self.book.isbn)

        self.ui.description_plainTextEdit.setPlainText(self.book.description)


    def editBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.isbn_lineEdit.text()
            author = session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex() + 1).first()
            category = session.query(Category).filter_by(id=self.ui.category_comboBox.currentIndex() + 1).first()

            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif category == None: raise NoInputException('Enter the category of the book')

            description = self.ui.description_plainTextEdit.toPlainText()

            updates = {
                'title': book_title,
                'isbn': isbn,
                'author_id': author.id,
                'category_id': category.id,
                'description': description
            }

            for key, value in updates.items():
                setattr(self.book, key, value)

            session.commit()


            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText('Book edited')
            message.exec_()

        except NoInputException as e:
            e.showMessage()
        except IntegrityError:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText('Field already inserted')
            error_message.setWindowTitle('Error')
            error_message.exec_()
            session.rollback()

    def deleteBook(self):
        session.delete(self.book)
        session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText('Book eliminated')
        message.exec_()
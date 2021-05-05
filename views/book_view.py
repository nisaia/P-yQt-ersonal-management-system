import sys
from PyQt5.QtWidgets import QWidget
from ui.book_window import *
from PyQt5.QtGui import QPixmap
from database.models import *
from database.db import session
from utils.custom_exceptions import *
from utils.functions import openDialog
from sqlalchemy.exc import IntegrityError
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from views.coverIllustration_view import *
from PyQt5.QtCore import QUrl
import os
from os.path import join
from utils.constants import COVER_PATH
import shutil


class BookView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_book_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.preview_button.clicked.connect(self.displayCover)

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        self.ui.coverPath_label.setText(file_name)

    def displayCover(self):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(self.ui.coverPath_label.text())
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)
        coverIllustration_window.ui.coverIllustration_label.setScaledContents(True)

        coverIllustration_window.exec_()

    def updateValues(self, book, author, genre):
        self.book = book
        self.author = author
        self.genre = genre

        self.ui.author_comboBox.clear()
        self.ui.genre_comboBox.clear()

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.author_comboBox.addItem('No authors founded')
            self.ui.author_comboBox.setDisabled(True)
        else:
            for author_item in authors:
                self.ui.author_comboBox.addItem(str(author_item.name + " " + author_item.surname))
            self.ui.author_comboBox.setDisabled(False)

        genres = session.query(Genre).all()
        if len(genres) == 0:
            self.ui.genre_comboBox.addItem('No genres founded')
            self.ui.genre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.genre_comboBox.addItem(genre.name)
            self.ui.genre_comboBox.setDisabled(False)

        # FIRST TAB
        self.ui.title.setText(self.book.title)
        self.ui.isbn.setText(self.book.isbn)
        image = QPixmap(self.book.cover_path)
        image = image.scaled(self.ui.cover.width(), self.ui.cover.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.cover.setPixmap(image)
        self.ui.cover.setScaledContents(True)
        self.ui.author.setText(self.author.name + " " + self.author.surname)
        self.ui.genre.setText(self.genre.name)
        self.ui.description.setText(self.book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(self.book.title)
        self.ui.isbn_lineEdit.setText(self.book.isbn)
        self.ui.coverPath_label.setText(self.book.cover_path)

        self.ui.author_comboBox.setCurrentIndex(self.author.id - 1)
        self.ui.genre_comboBox.setCurrentIndex(self.genre.id - 1)

        self.ui.description_plainTextEdit.setPlainText(self.book.description)


    def editBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.isbn_lineEdit.text()
            author = session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex() + 1).first()
            genre = session.query(Genre).filter_by(id=self.ui.genre_comboBox.currentIndex() + 1).first()

            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif genre == None: raise NoInputException('Enter the genre of the book')

            cover_path = self.ui.coverPath_label.text()
            book_cover_path = self.book.cover_path

            if cover_path != book_cover_path:
                file_name = QUrl.fromLocalFile(cover_path).fileName()
                print(file_name)
                new_cover_path = join(COVER_PATH, file_name)
                os.remove(book_cover_path)
                shutil.copy(cover_path, new_cover_path)
            else:
                new_cover_path = self.book.cover_path

            description = self.ui.description_plainTextEdit.toPlainText()

            updates = {
                'title': book_title,
                'isbn': isbn,
                'author_id': author.id,
                'genre_id': genre.id,
                'cover_path': new_cover_path,
                'description': description
            }

            for key, value in updates.items():
                setattr(self.book, key, value)

            session.commit()

            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)

            openDialog(QMessageBox.Information, 'Book edited', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Field already inserted', 'Error')
            session.rollback()

    def deleteBook(self):
        session.delete(self.book)
        session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Book deleted', 'Success')
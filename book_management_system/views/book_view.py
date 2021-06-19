import sys
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog
from book_management_system.ui.book_window import *
from PyQt5.QtGui import QPixmap
from database.book_models import *
from database.db import book_session
from book_management_system.utils.custom_exceptions import *
from book_management_system.utils.functions import openDialog
from sqlalchemy.exc import IntegrityError
from book_management_system.views.coverIllustration_view import *
from PyQt5.QtCore import QUrl
import os
from os.path import join
from book_management_system.utils.constants import COVER_PATH
import shutil


class BookView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_book_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.bookPreview_button.clicked.connect(self.displayCover)

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.findChild(QtWidgets.QTabWidget).tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        self.show()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        self.ui.bookCoverPath_label.setText(file_name)

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

        self.ui.bookAuthor_comboBox.clear()
        self.ui.bookGenre_comboBox.clear()

        authors = book_session.query(Author).all()
        if len(authors) == 0:
            self.ui.bookAuthor_comboBox.addItem('No authors founded')
            self.ui.bookAuthor_comboBox.setDisabled(True)
        else:
            for author_item in authors:
                self.ui.bookAuthor_comboBox.addItem(str(author_item.name + " " + author_item.surname))
            self.ui.bookAuthor_comboBox.setDisabled(False)

        genres = book_session.query(Genre).all()
        if len(genres) == 0:
            self.ui.bookGenre_comboBox.addItem('No genres founded')
            self.ui.bookGenre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.bookGenre_comboBox.addItem(genre.name)
            self.ui.bookGenre_comboBox.setDisabled(False)

        # FIRST TAB
        self.ui.bookTitle_label.setText(self.book.title)
        self.ui.bookIsbn_label.setText(self.book.isbn)
        image = QPixmap(self.book.cover_path)
        image = image.scaled(self.ui.bookCover_label.width(), self.ui.bookCover_label.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.bookCover_label.setPixmap(image)
        self.ui.bookCover_label.setScaledContents(True)

        self.ui.bookAuthor_label.setText(self.author.name + ' ' + self.author.surname)
        self.ui.bookGenre_label.setText(self.genre.name)
        self.ui.bookDescription_label.setText(self.book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(self.book.title)
        self.ui.bookIsbn_lineEdit.setText(self.book.isbn)
        self.ui.bookCoverPath_label.setText(self.book.cover_path)

        self.ui.bookAuthor_comboBox.setCurrentIndex(self.author.id - 1)
        self.ui.bookGenre_comboBox.setCurrentIndex(self.genre.id - 1)

        self.ui.bookDescription_plainTextEdit.setPlainText(self.book.description)


    def editBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.bookIsbn_lineEdit.text()
            author = book_session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex() + 1).first()
            genre = book_session.query(Genre).filter_by(id=self.ui.genre_comboBox.currentIndex() + 1).first()

            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif genre == None: raise NoInputException('Enter the genre of the book')

            cover_path = self.ui.bookCoverPath_label.text()
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

            book_session.commit()

            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)

            openDialog(QMessageBox.Information, 'Book edited', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Field already inserted', 'Error')
            book_session.rollback()

    def deleteBook(self):
        book_session.delete(self.book)
        book_session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Book deleted', 'Success')
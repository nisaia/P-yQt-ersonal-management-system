import sys
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog
from book_management_system.ui.book_window import *
from PyQt5.QtGui import QPixmap
from database.book_models import *
from database.db import book_session
from utils.custom_exceptions import *
from utils.functions import openDialog, displayCover, get_image_file
from sqlalchemy.exc import IntegrityError
from book_management_system.views.coverIllustration_view import *
from PyQt5.QtCore import QUrl
import os
from os.path import join
from utils.constants import COVER_PATH, NO_COVER_AVAILABLE_PATH, BOOK_ICONS_PATH, FIRST_YEAR_BOOK, ACTUAL_YEAR
import shutil


class BookView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_book_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(lambda: get_image_file(parent=self, label=self.ui.bookCoverPath_label, button=self.ui.bookPreview_button))
        self.ui.bookPreview_button.clicked.connect(lambda: displayCover(label=self.ui.bookCoverPath_label))

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        isbnIcon = QPixmap(join(BOOK_ICONS_PATH, 'isbn.png'))
        self.ui.bookIsbnIcon_label.setPixmap(isbnIcon)

        pagesIcon = QPixmap(join(BOOK_ICONS_PATH, 'pages.png'))
        self.ui.bookPagesIcon_label.setPixmap(pagesIcon)

        yearIcon = QPixmap(join(BOOK_ICONS_PATH, 'release.png'))
        self.ui.bookYearIcon_label.setPixmap(yearIcon)

        genreIcon = QPixmap(join(BOOK_ICONS_PATH, 'genre.png'))
        self.ui.bookGenreIcon_label.setPixmap(genreIcon)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.findChild(QtWidgets.QTabWidget).tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        self.show()

    def updateValues(self, book, author, genre, status):
        self.book = book
        self.author = author
        self.genre = genre
        self.status = status

        self.ui.bookYear_comboBox.clear()
        self.ui.bookAuthor_comboBox.clear()
        self.ui.bookGenre_comboBox.clear()
        self.ui.bookStatus_comboBox.clear()

        for year in range(FIRST_YEAR_BOOK, ACTUAL_YEAR):
            self.ui.bookYear_comboBox.addItem(str(year))
    
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

        all_status = book_session.query(BookStatus).all()
        for status in all_status:
            self.ui.bookStatus_comboBox.addItem(status.name)

        # FIRST TAB

        self.ui.bookTitle_label.setText(self.book.title + ', ' + self.author.name + ' ' + self.author.surname)
        self.ui.bookIsbn_label.setText(self.book.isbn)
        self.ui.bookPages_label_2.setText(str(self.book.pages))
        self.ui.bookYear_label_2.setText(str(self.book.year))
        image = QPixmap(self.book.cover_path)
        image = image.scaled(self.ui.bookCover_label.width(), self.ui.bookCover_label.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.bookCover_label.setPixmap(image)
        self.ui.bookCover_label.setScaledContents(True)

        #self.ui.bookAuthor_label.setText(self.author.name + ' ' + self.author.surname)
        self.ui.bookGenre_label.setText(self.genre.name)
        self.ui.bookDescription_label.setText(self.book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(self.book.title)
        self.ui.bookIsbn_lineEdit.setText(self.book.isbn)
        self.ui.bookPages_lineEdit.setText(str(self.book.pages))
        self.ui.bookCoverPath_label.setText(self.book.cover_path)

        self.ui.bookYear_comboBox.setCurrentText(str(self.book.year))
        self.ui.bookAuthor_comboBox.setCurrentIndex(self.author.id - 1)
        self.ui.bookGenre_comboBox.setCurrentIndex(self.genre.id - 1)
        self.ui.bookStatus_comboBox.setCurrentIndex(self.status.id -1)

        self.ui.bookDescription_plainTextEdit.setPlainText(self.book.description)
        


    def editBook(self):
        try:
            book_title = self.ui.bookTitle_lineEdit.text()
            isbn = self.ui.bookIsbn_lineEdit.text()
            pages = self.ui.bookPages_lineEdit.text()
            year = str(self.ui.bookYear_comboBox.currentText())
            author = book_session.query(Author).filter_by(id=self.ui.bookAuthor_comboBox.currentIndex() + 1).first()
            genre = book_session.query(Genre).filter_by(id=self.ui.bookGenre_comboBox.currentIndex() + 1).first()
            status = book_session.query(BookStatus).filter_by(id=self.ui.bookStatus_comboBox.currentIndex() + 1).first()


            if len(book_title) == 0: raise NoInputException('Enter the title of book')
            elif len(isbn) == 0: raise NoInputException('Enter the ISBN of book')
            elif len(pages) == 0: raise NoInputException('Enter book number pages')
            elif author == None: raise NoInputException('Enter the author of the book')
            elif genre == None: raise NoInputException('Enter the genre of the book')

            if not pages.isdigit(): raise NoNumericInputException('Pages value not valid')

            cover_path = self.ui.bookCoverPath_label.text()
            book_cover_path = self.book.cover_path

            if cover_path != book_cover_path:
                file_name = QUrl.fromLocalFile(cover_path).fileName()
                print(file_name)
                new_cover_path = join(COVER_PATH, file_name)
                shutil.copy(cover_path, new_cover_path)
                if cover_path != NO_COVER_AVAILABLE_PATH:
                    os.remove(book_cover_path)
            else:
                new_cover_path = self.book.cover_path

            description = self.ui.bookDescription_plainTextEdit.toPlainText()

            updates = {
                'title': book_title,
                'isbn': isbn,
                'pages': pages,
                'year': year,
                'author_id': author.id,
                'genre_id': genre.id,
                'cover_path': new_cover_path,
                'status_id': status.id,
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
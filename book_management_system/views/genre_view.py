import sys
from PyQt5.QtWidgets import QWidget
from database.db import book_session
from database.book_models import *
from database.book_models import Genre
from utils.custom_exceptions import *
from utils.functions import openDialog
from sqlalchemy.exc import IntegrityError
from book_management_system.ui.genre_window import *

class GenreView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        
        self.ui = Ui_genre_window()
        self.ui.setupUi(self)

        self.ui.editGenre_button.clicked.connect(self.editGenre)
        self.ui.deleteGenre_button.clicked.connect(self.deleteGenre)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def updateValues(self, genre):
        self.genre = genre
        self.ui.genreName_lineEdit.setText(self.genre.name)

    def editGenre(self):
        try:
            genre_name = self.ui.genreName_lineEdit.text()
            
            if len(genre_name) == 0: raise NoInputException('Enter the name of the genre')

            setattr(self.genre, 'name', genre_name)

            book_session.commit()

            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)

            openDialog(QMessageBox.Information, 'Genre edited', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message,'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Field already inserted', 'Error')
            book_session.rollback()

    def deleteGenre(self):

        books = book_session.query(Book).filter_by(genre_id=self.genre.id).all()

        for book in books:
            book_session.delete(book)

        book_session.delete(self.genre)
        book_session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Genre deleted', 'Success')
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from movie_management_system.ui.addGenre_window import *
from database.db import movie_session
from database.movie_models import Genre
from utils.custom_exceptions import NoInputException
from utils.functions import openDialog
from sqlalchemy.exc import IntegrityError

class AddGenreView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addGenre_window()
        self.ui.setupUi(self)

        self.ui.addGenre_button.clicked.connect(self.addGenre)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def addGenre(self):
        try:
            name = self.ui.genreName_lineEdit.text()
            if len(name) == 0: raise NoInputException('Enter genre name')

            genre = Genre(name=name)
            movie_session.add(genre)
            movie_session.commit()

            self.clearField()
            openDialog(QMessageBox.Information, 'Genre inserted', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Genre already inserted', 'Error')
            movie_session.rollback()

    def clearField(self):
        self.ui.genreName_lineEdit.clear()
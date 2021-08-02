import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from movie_management_system.ui.addFilmDirector_window import *
from database.db import movie_session
from database.movie_models import Film_director
from utils.custom_exceptions import *
from utils.functions import openDialog

class AddFilmDirectorView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addFilmDirector_window()
        self.ui.setupUi(self)

        self.ui.addFilmDirector_button.clicked.connect(self.addFilmDirector)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def addFilmDirector(self):
        try:
            name = self.ui.filmDirectorName_lineEdit.text()
            surname = self.ui.filmDirectorSurname_lineEdit.text()

            if len(name) == 0: raise NoInputException('Enter film director name')
            if len(surname) == 0: raise NoInputException('Enter film director surname')

            filmDirector = Film_director(name=name, surname=surname)
            movie_session.add(filmDirector)
            movie_session.commit()

            self.clearAll()
            openDialog(QMessageBox.Information, 'Film director inserted', 'Success')

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')

    def clearAll(self):
        self.ui.filmDirectorName_lineEdit.clear()
        self.ui.filmDirectorSurname_lineEdit.clear()
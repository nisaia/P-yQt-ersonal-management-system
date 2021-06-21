import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from book_management_system.ui.addGenre_window import *
from database.db import book_session
from database.book_models import Genre
from utils.custom_exceptions import NoInputException
from utils.functions import openDialog
from sqlalchemy.exc import IntegrityError

class AddGenreView(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addGenre_window()
        self.ui.setupUi(self)

        self.ui.addGenre_button_1.clicked.connect(self.addCategory)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def addCategory(self):
        try:
            name = self.ui.genreName_lineEdit.text()
            if len(name) == 0: raise NoInputException('Enter category name')

            genre = Genre(name=name)
            book_session.add(genre)
            book_session.commit()

            self.clearField()
            openDialog(QMessageBox.Information, 'Genre inserted', 'Success')
            
        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Genre already inserted', 'Error')
            book_session.rollback()

    def clearField(self):
        self.ui.genreName_lineEdit.clear()
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from assets.ui_PY.addAuthor_window import *
from database.db import session
from database.models import Author
from utils.custom_exceptions import *

class AddAuthorView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addAuthor_window()
        self.ui.setupUi(self)

        self.ui.addAuthor_button.clicked.connect(self.addAuthor)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

    def addAuthor(self):
        try:
            name = self.ui.authorName_lineEdit.text()
            surname = self.ui.authorSurname_lineEdit.text()

            if len(name) == 0: raise NoInputException('Enter author name')
            if len(surname) == 0: raise NoInputException('Enter author surname')

            author = Author(name=name, surname=surname)
            session.add(author)
            session.commit()

            self.clearAll()

        except NoInputException as e:
            message = e.error_message
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText(message)
            error_message.setWindowTitle('Error')
            error_message.exec_()

    def clearAll(self):
        self.ui.authorName_lineEdit.clear()
        self.ui.authorSurname_lineEdit.clear()
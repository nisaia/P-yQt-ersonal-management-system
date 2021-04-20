import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from assets.ui_PY.addCategory_window import *
from database.db import session
from database.models import Category
from utils.custom_exceptions import NoInputException
from sqlalchemy.exc import IntegrityError

class AddCategoryView(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_addCategory_window()
        self.ui.setupUi(self)

        self.ui.addCategory_button.clicked.connect(self.addCategory)

        self.show()

    def addCategory(self):
        try:
            name = self.ui.categoryName_lineEdit.text()
            if len(name) == 0: raise NoInputException('Enter category name')

            category = Category(name=name)
            session.add(category)
            session.commit()

            self.clearField()
        except NoInputException as e:
            message = e.error_message
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText(message)
            error_message.setWindowTitle('Error')
            error_message.exec_()
        except IntegrityError:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText('Category already inserted')
            error_message.setWindowTitle('Error')
            error_message.exec_()
            session.rollback()

    def clearField(self):
        self.ui.categoryName_lineEdit.clear()


    def clearAll(self):
        self.ui.categoryName_lineEdit.clear()
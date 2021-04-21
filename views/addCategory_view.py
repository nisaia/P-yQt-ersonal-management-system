import sys
from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.addCategory_window import *
from database.db import session
from database.models import Category
from utils.custom_exceptions import NoInputException
from utils.functions import openDialog
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
            openDialog(QMessageBox.Information, 'Category inserted', 'Success')
            
        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Category already inserted', 'Error')
            session.rollback()

    def clearField(self):
        self.ui.categoryName_lineEdit.clear()
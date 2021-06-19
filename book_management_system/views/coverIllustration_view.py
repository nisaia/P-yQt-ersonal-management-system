import sys
from PyQt5.QtWidgets import QDialog, QApplication
from book_management_system.ui.coverIllustration_window import *

class CoverIllustrationView(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_coverIllustration_window()
        self.ui.setupUi(self)

        self.show()
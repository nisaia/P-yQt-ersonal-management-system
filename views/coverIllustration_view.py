import sys
from PyQt5.QtWidgets import QDialog, QApplication
from assets.ui_PY.coverIllustration_window import *

class CoverIllustrationView(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.show()
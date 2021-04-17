import sys
from PyQt5.QtWidgets import QWidget
from assets.ui_PY.home_window import *

class HomeView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()
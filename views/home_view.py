import sys
from PyQt5.QtWidgets import QWidget
from ui.home_window import *

class HomeView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_home_window()
        self.ui.setupUi(self)

        self.show()
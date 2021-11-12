import sys
from movie_management_system.ui.movie_window import *
from PyQt5.QtWidgets import QWidget

class MovieView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_movie_window()
        self.ui.setupUi(self)

        self.show()
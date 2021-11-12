import sys
from movie_management_system.ui.statistics_window import *
from PyQt5.QtWidgets import QWidget

class StatisticsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_statistics_window()
        self.ui.setupUi(self)

        self.show()
import sys

from movie_management_system.ui.main_window import *
from PyQt5.QtWidgets import QApplication, QWidget
from movie_management_system.views.addMovie_view import AddMovieView

class MovieMainView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.addMovie_view = AddMovieView(parent=self)

        self.ui.stackedWidget.addWidget(self.addMovie_view)

        self.ui.addMovie_button.clicked.connect(self.addMovie)

        self.show()

    def addMovie(self):
        self.addMovie_view.updateComboBox()
        self.ui.stackedWidget.setCurrentWidget(self.addMovie_view)
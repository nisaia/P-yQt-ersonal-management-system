import sys

from movie_management_system.ui.main_window import *
from PyQt5.QtWidgets import QApplication, QWidget
from movie_management_system.views.addMovie_view import AddMovieView
from movie_management_system.views.home_view import HomeView
from movie_management_system.views.allMovies_view import AllMoviesView
from movie_management_system.views.addFilmDirector_view import AddFilmDirectorView
from movie_management_system.views.addGenre_view import AddGenreView

class MovieMainView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.addMovie_view = AddMovieView(parent=self)
        self.home_view = HomeView(parent=self)
        self.allMovies_view = AllMoviesView(parent=self)
        self.addFilmDirector_view = AddFilmDirectorView(parent=self)
        self.addGenre_view = AddGenreView(parent=self)

        self.ui.stackedWidget.addWidget(self.addMovie_view)
        self.ui.stackedWidget.addWidget(self.home_view)
        self.ui.stackedWidget.addWidget(self.allMovies_view)
        self.ui.stackedWidget.addWidget(self.addFilmDirector_view)
        self.ui.stackedWidget.addWidget(self.addGenre_view)

        self.ui.addMovie_button.clicked.connect(self.addMovie)
        self.ui.home_button.clicked.connect(self.home)
        self.ui.allMovies_button.clicked.connect(self.allMovies)
        self.ui.addFilmDirector_button.clicked.connect(self.addFilmDirector)
        self.ui.addGenre_button.clicked.connect(self.addGenre)

        self.ui.stackedWidget.setCurrentWidget(self.home_view)

        self.show()

    def addMovie(self):
        self.addMovie_view.updateComboBox()
        self.ui.stackedWidget.setCurrentWidget(self.addMovie_view)

    def home(self):
        self.ui.stackedWidget.setCurrentWidget(self.home_view)

    def allMovies(self):
        self.allMovies_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allMovies_view)

    def addFilmDirector(self):
        self.ui.stackedWidget.setCurrentWidget(self.addFilmDirector_view)

    def addGenre(self):
        self.ui.stackedWidget.setCurrentWidget(self.addGenre_view)
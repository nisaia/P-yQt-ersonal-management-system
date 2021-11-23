import sys

from movie_management_system.ui.main_window import *
from PyQt5.QtWidgets import QApplication, QWidget
from movie_management_system.views.addMovie_view import AddMovieView
from movie_management_system.views.home_view import HomeView
from movie_management_system.views.allMovies_view import AllMoviesView
from movie_management_system.views.movie_view import MovieView
from movie_management_system.views.addFilmDirector_view import AddFilmDirectorView
from movie_management_system.views.addGenre_view import AddGenreView
from movie_management_system.views.allFilmDirectors_view import AllFilmDirectorsView
from movie_management_system.views.allGenres_view import AllGenresView
from movie_management_system.views.filmDirector_view import FilmDirectorView
from movie_management_system.views.genre_view import GenreView
from movie_management_system.views.movie_view import MovieView
from movie_management_system.views.statistics_view import StatisticsView

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
        self.allFilmDirectors_view = AllFilmDirectorsView(parent=self)
        self.allGenres_view = AllGenresView(parent=self)
        self.filmDirector_view = FilmDirectorView(parent=self)
        self.genre_view = GenreView(parent=self)
        self.movie_view = MovieView(parent=self)
        self.statistics_view = StatisticsView(parent=self)

        self.ui.stackedWidget.addWidget(self.addMovie_view)
        self.ui.stackedWidget.addWidget(self.home_view)
        self.ui.stackedWidget.addWidget(self.allMovies_view)
        self.ui.stackedWidget.addWidget(self.movie_view)
        self.ui.stackedWidget.addWidget(self.addFilmDirector_view)
        self.ui.stackedWidget.addWidget(self.addGenre_view)
        self.ui.stackedWidget.addWidget(self.allFilmDirectors_view)
        self.ui.stackedWidget.addWidget(self.allGenres_view)
        self.ui.stackedWidget.addWidget(self.filmDirector_view)
        self.ui.stackedWidget.addWidget(self.genre_view)
        self.ui.stackedWidget.addWidget(self.movie_view)
        self.ui.stackedWidget.addWidget(self.statistics_view)

        self.ui.addMovie_button.clicked.connect(self.addMovie)
        self.ui.home_button.clicked.connect(self.home)
        self.ui.allMovies_button.clicked.connect(self.allMovies)
        self.ui.addFilmDirector_button.clicked.connect(self.addFilmDirector)
        self.ui.addGenre_button.clicked.connect(self.addGenre)
        self.ui.allFilmDirectors_button.clicked.connect(self.allFilmDirectors)
        self.ui.allGenres_button.clicked.connect(self.allGenres)
        self.ui.statistics_button.clicked.connect(self.getStatistics)

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

    def allFilmDirectors(self):
        self.allFilmDirectors_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allFilmDirectors_view)

    def allGenres(self):
        self.allGenres_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allGenres_view)

    def getStatistics(self):
        self.statistics_view.getValues()
        self.statistics_view.updateValues()
        self.ui.stackedWidget.setCurrentWidget(self.statistics_view)
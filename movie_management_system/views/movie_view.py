import sys
from movie_management_system.ui.movie_window import *
from utils.functions import displayCover, get_image_file
from utils.constants import FIRST_YEAR_MOVIE, ACTUAL_YEAR
from PyQt5.QtWidgets import QWidget
from database.db import movie_session
from database.movie_models import *
from PyQt5.QtGui import QPixmap

class MovieView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_movie_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(lambda: get_image_file(parent=self, label=self.ui.movieCoverPath_label, button=self.ui.moviePreview_button))
        self.ui.moviePreview_button.clicked.connect(lambda: displayCover(label=self.ui.movieCoverPath_label))

        self.ui.editMovie_button.clicked.connect(self.editMovie)
        self.ui.deleteMovie_button.clicked.connect(self.deleteMovie)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.findChild(QtWidgets.QTabWidget).tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        self.show()

    def updateValues(self, movie, film_director, genre, status):
        self.movie = movie
        self.film_director = film_director
        self.genre = genre
        self.status = status

        self.ui.movieYear_comboBox.clear()
        self.ui.filmDirector_comboBox.clear()
        self.ui.movieGenre_comboBox.clear()
        self.ui.movieStatus_comboBox.clear()

        for year in range(FIRST_YEAR_MOVIE, ACTUAL_YEAR):
            self.ui.movieYear_comboBox.addItem(str(year))

        film_directors = movie_session.query(Film_director).all()
        if len(film_directors) == 0:
            self.ui.filmDirector_comboBox.addItem('No authors founded')
            self.ui.filmDirector_comboBox.setDisabled(True)
        else:
            for film_director in film_directors:
                self.ui.filmDirector_comboBox.addItem(str(film_director.name + ' ' + film_director.surname))
            self.ui.filmDirector_comboBox.setDisabled(False)

        genres = movie_session.query(Genre).all()
        if len(genres) == 0:
            self.ui.movieGenre_comboBox.addItem('No genres founded')
            self.ui.movieGenre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.movieGenre_comboBox.addItem(genre.name)
            self.ui.movieGenre_comboBox.setDisabled(False)

        all_status = movie_session.query(MovieStatus).all()
        for status in all_status:
            self.ui.movieStatus_comboBox.addItem(status.name)

        hour = self.movie.film_length // 60
        minutes = self.movie.film_length % 60

        # FIRST TAB
        self.ui.movieTitle_label.setText(self.movie.title + ', ' + self.film_director.name + ' ' + self.film_director.surname)
        self.ui.movieLength_label.setText(str(hour) + ' hour, ' + str(minutes) + ' minutes')
        self.ui.movieYear_label.setText(str(self.movie.year))
        image = QPixmap(self.movie.cover_path)
        image = image.scaled(self.ui.movieCover_label.width(), self.ui.movieCover_label.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.movieCover_label.setPixmap(image)
        self.ui.movieCover_label.setScaledContents(True)
        self.ui.movieGenre_label.setText(self.genre.name)
        self.ui.movieDescription_label.setText(self.movie.description)

        # SECOND TAB
        self.ui.movieTitle_lineEdit.setText(self.movie.title)
        self.ui.movieCoverPath_label.setText(self.movie.cover_path)

        self.ui.hour_spinBox.setValue(self.movie.film_length // 60)
        self.ui.minutes_spinBox.setValue(self.movie.film_length % 60) 

        self.ui.movieYear_comboBox.setCurrentText(str(self.movie.year))
        self.ui.filmDirector_comboBox.setCurrentIndex(self.film_director.id - 1)
        self.ui.movieGenre_comboBox.setCurrentIndex(self.genre.id - 1)
        self.ui.movieStatus_comboBox.setCurrentIndex(self.status.id - 1)

        self.ui.movieDescription_plainTextEdit.setPlainText(self.movie.description)

    def editMovie(self): pass
    def deleteMovie(self): pass
import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QMainWindow, QDialog
from movie_management_system.ui.addMovie_window import *
from database.db import movie_session
from database.movie_models import *
from PyQt5.QtGui import QPixmap
from utils.custom_exceptions import NoInputException
from sqlalchemy.exc import IntegrityError
from utils.constants import COVER_PATH
from os.path import join
from utils.functions import openDialog
import datetime

class AddMovieView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_addMovie_window()
        self.ui.setupUi(self)

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
        self.ui.moviePreview_button.clicked.connect(self.displayCover)

        self.ui.addMovie_button.clicked.connect(self.addMovie)
        self.ui.clearAll_button.clicked.connect(self.clearAll)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        for combobox in self.findChildren(QtWidgets.QComboBox):
            combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def updateComboBox(self):
        print("diocane")
        self.ui.movieYear_comboBox.clear()
        self.ui.filmDirector_comboBox.clear()
        self.ui.movieGenre_comboBox.clear()

        # 1888 ANNO DI USCITA PRIMO FILM DEL CINEMA
        for year in range(1888, datetime.datetime.now().year + 1):
            self.ui.movieYear_comboBox.addItem(str(year))

        filmDirectors = movie_session.query(Film_director).all()
        if len(filmDirectors) == 0:
            self.ui.filmDirector_comboBox.addItem('No film directors founded')
            self.ui.filmDirector_comboBox.setDisabled(True)
        else:
            for filmDirector in filmDirectors:
                self.ui.filmDirector_comboBox.addItem(str(filmDirector.name + " " + filmDirector.surname))
            self.ui.filmDirector_comboBox.setDisabled(False)

        genres = movie_session.query(Genre).all()
        if len(genres) == 0:
            self.ui.movieGenre_comboBox.addItem('No genres founded')
            self.ui.movieGenre_comboBox.setDisabled(True)
        else:
            for genre in genres:
                self.ui.movieGenre_comboBox.addItem(genre.name)
            self.ui.movieGenre_comboBox.setDisabled(False)

    def get_image_file(self): pass

    def displayCover(self): pass

    def addMovie(self): pass

    def clearAll(self): pass

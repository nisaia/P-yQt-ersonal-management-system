import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QMainWindow, QDialog
from movie_management_system.ui.addMovie_window import *
from database.db import movie_session
from database.movie_models import *
from PyQt5.QtGui import QPixmap
from utils.custom_exceptions import NoInputException
from sqlalchemy.exc import IntegrityError
from utils.constants import COVER_PATH, FIRST_YEAR_MOVIE, ACTUAL_YEAR, NO_COVER_AVAILABLE_PATH
from os.path import join
from utils.functions import openDialog
import datetime
import shutil

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
        self.ui.movieYear_comboBox.clear()
        self.ui.filmDirector_comboBox.clear()
        self.ui.movieGenre_comboBox.clear()

        # 1888 ANNO DI USCITA PRIMO FILM DEL CINEMA
        for year in range(FIRST_YEAR_MOVIE, ACTUAL_YEAR + 1):
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

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open image file', r"/", "Image files (*.jpg *.png)")
        if len(file_name) != 0:
            self.ui.movieCoverPath_label.setText(file_name)
            self.ui.movieCoverPath_label.setVisible(True)
            self.ui.moviePreview_button.setVisible(True)

    def displayCover(self): pass

    def addMovie(self):
        try:
            movie_title = self.ui.movieTitle_lineEdit.text()
            movie_year = int(self.ui.movieYear_comboBox.currentText())
            film_director = movie_session.query(Film_director).filter_by(id=self.ui.filmDirector_comboBox.currentIndex() + 1).first()
            genre = movie_session.query(Genre).filter_by(id=self.ui.movieGenre_comboBox.currentIndex() + 1).first()
            cover_path = self.ui.movieCoverPath_label.text()
            description = self.ui.movieDescription_plainTextEdit.toPlainText()

            if len(movie_title) == 0: raise NoInputException('Enter the title of movie')
            elif film_director == None: raise NoInputException('Enter the film director of the movie')
            elif genre == None: raise NoInputException('Enter the genre of the movie')
            
            if len(cover_path) == 0:
                new_cover_path = NO_COVER_AVAILABLE_PATH
            else:
                file_name = QUrl.fromLocalFile(cover_path).fileName()
                new_cover_path = join(COVER_PATH, file_name)
                shutil.copy(cover_path, new_cover_path)

            movie = Movie(title=movie_title,
                          year=movie_year,
                          film_director_id=film_director.id,
                          genre_id=genre.id,
                          description=description,
                          cover_path=cover_path)
            movie_session.add(movie)
            movie_session.commit()

            self.clearAll()

            openDialog(QMessageBox.Information, 'Movie added', 'Success')
            
        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')
        except IntegrityError:
            openDialog(QMessageBox.Critical, 'Movie already inserted', 'Error')
            movie_session.rollback()

    def clearAll(self):
        self.ui.movieTitle_lineEdit.clear()
        self.ui.movieYear_comboBox.setCurrentIndex(0)
        self.ui.filmDirector_comboBox.setCurrentIndex(0)
        self.ui.movieGenre_comboBox.setCurrentIndex(0)
        self.ui.movieCoverPath_label.setText("")
        self.ui.movieCoverPath_label.setVisible(False)
        self.ui.moviePreview_button.setVisible(False)
        self.ui.movieDescription_plainTextEdit.clear()
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from movie_management_system.ui.filmDirector_window import *
from database.movie_models import Film_director, Movie
from database.db import movie_session
from utils.custom_exceptions import *
from utils.functions import openDialog

class FilmDirectorView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_filmDirector_window()
        self.ui.setupUi(self)

        self.ui.editFilmDirector_button.clicked.connect(self.editFilmDirector)
        self.ui.deleteFilmDirector_button.clicked.connect(self.deleteFilmDirector)

        self.findChild(QtWidgets.QTabWidget).tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        self.show()

    def updateValues(self, filmDirector):
        self.filmDirector = filmDirector

        #FIRST TAB
        self.ui.filmDirectorName_label.setText(self.filmDirector.name)
        self.ui.filmDirectorSurname_label.setText(self.filmDirector.surname)

        linkTemplate = '<a href={0}>{1}</a>'
        wikipedia_header = 'https://it.wikipedia.org/wiki/'
        filmDirector_url = self.filmDirector.name + '_' + self.filmDirector.surname

        self.ui.filmDirectorWikipedia_label.setText(linkTemplate.format(wikipedia_header + filmDirector_url, filmDirector_url.replace('_', ' ')))

        #SECONDO TAB
        self.ui.filmDirectorName_lineEdit.setText(self.filmDirector.name)
        self.ui.filmDirectorSurname_lineEdit.setText(self.filmDirector.surname)

    def editFilmDirector(self):
        try:
            name = self.ui.filmDirectorName_lineEdit.text()
            surname = self.ui.filmDirectorSurname_lineEdit.text()

            if len(name) == 0: raise NoInputException('Enter name of the author')
            elif len(surname) == 0 raise NoInputException('Enter surname of the author')

            if self.filmDirector.name != name or self.filmDirector.surname != surname:
                updates = {
                    'name': name,
                    'surname': surname
                }

                for key, value in updates.items():
                    setattr(self.filmDirector, key, vale)

                movie_session.commit()
                openDialog(QMessageBox.Information, 'Film director edited', 'Success')
            else:
                openDialog(QMessageBox.Information, 'Nothing changed', 'Success')

            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)

        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')

    def deleteFilmDirector(self):

        #CANCELLO TUTTI I FILM ASSOCIATI AL REGISTA
        movies = movie_session.query(Movie).filter_by(film_director_id=self.film_director_id).all()

        for movie in movies:
            movie_session.delete(movie)

        movie_session.delete(self.filmDirector)

        movie_session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Film director deleted', 'Success')
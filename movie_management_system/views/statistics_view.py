import sys

from movie_management_system.ui.statistics_window import *
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QPainter, QColor
from database.db import movie_session
from database.movie_models import *
from utils.functions import openDialog

class StatisticsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_statistics_window()
        self.ui.setupUi(self)

        self.genre_series = QPieSeries()
        self.filmDirector_series = QPieSeries()
        self.status_series = QPieSeries()

        self.createChart('Movie percentages genre', self.genre_series)
        self.createChart('Movie percentages film director', self.filmDirector_series)
        self.createChart('Movie percentages status', self.status_series)

        self.show()

    def getValues(self):
        movies = movie_session.query(Movie).count()
        filmDirectors = movie_session.query(Film_director).count()
        genres = movie_session.query(Genre).count()

        self.ui.moviesCounter_label.setText(str(movies))
        self.ui.filmDirectorsCounter_label.setText(str(filmDirectors))
        self.ui.genresCounter_label.setText(str(genres))

    def createChart(self, title, series):

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle(title)

            #sslice.setLabel("{:.1f}%".format(100 * slice.percentage()))

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        #setChart(chartview)
        self.ui.pieChart_container.addWidget(chartview)

    def updateValues(self):
        try:
            counter_movies = movie_session.query(Movie).count()

            genres = movie_session.query(Genre).all()
            self.genre_series.clear()
            for genre in genres:
                genre_movies = movie_session.query(Movie).filter_by(genre_id=genre.id).count()
                self.genre_series.append(genre.name, genre_movies/counter_movies)

            for i in range(len(self.genre_series)):
                slice = QPieSlice()
                slice = self.genre_series.slices()[i]
                slice.setLabelVisible(True)

            film_directors = movie_session.query(Film_director).all()
            self.filmDirector_series.clear()
            for film_director in film_directors:
                filmDirector_movie = movie_session.query(Movie).filter_by(film_director_id=film_director.id).count()
                self.filmDirector_series.append(film_director.name + " " + film_director.surname, filmDirector_movie/counter_movies)

            for i in range(len(self.filmDirector_series)):
                slice = QPieSlice()
                slice = self.filmDirector_series.slices()[i]
                slice.setLabelVisible(True)

            self.status_series.clear()
            all_status = movie_session.query(MovieStatus).all()
            counter_status = {}
            for status in all_status:
                movie_status = movie_session.query(Movie).filter_by(status_id = status.id).count()
                self.status_series.append(status.name, movie_status/counter_movies)

            for i in range(len(self.status_series)):
                slice = QPieSlice()
                slice = self.status_series.slices()[i]
                slice.setLabelVisible(True)
                if slice.label() == 'Not watched':
                    slice.setColor(QColor(255, 0, 0))
                elif slice.label() == 'Watched':
                    slice.setColor(QColor(0, 100, 0))
        
        except ZeroDivisionError:
            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)
            openDialog(QMessageBox.Critical, 'Insufficient data for chart', 'Error')

            
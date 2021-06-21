import sys

from book_management_system.ui.statistics_window import *
from PyQt5.QtWidgets import QWidget, QMessageBox
from database.db import book_session
from database.book_models import *
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QPainter
from utils.functions import openDialog


class StatisticsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_statistics_window()
        self.ui.setupUi(self)

        self.genre_series = QPieSeries()
        self.author_series = QPieSeries()

        self.createChart('Book percentages genre', self.genre_series)
        self.createChart('Book percentages author', self.author_series)

        self.show()

    def getValues(self):
        books = book_session.query(Book).count()
        authors = book_session.query(Author).count()
        genres = book_session.query(Genre).count()

        self.ui.booksCounter_label.setText(str(books))
        self.ui.authorsCounter_label.setText(str(authors))
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
        self.ui.horizontalLayout.addWidget(chartview)

    def updateValues(self):
        try:

            books = book_session.query(Book).count()

            genres = book_session.query(Genre).all()
            self.genre_series.clear()
            for genre in genres:
                genre_books = book_session.query(Book).filter_by(genre_id=genre.id).count()
                self.genre_series.append(genre.name, genre_books/books)

            for i in range(len(self.genre_series)):
                slice = QPieSlice()
                slice = self.genre_series.slices()[i]
                slice.setLabelVisible(True)

            authors = book_session.query(Author).all()
            self.author_series.clear()
            for author in authors:
                author_books = book_session.query(Book).filter_by(author_id=author.id).count()
                self.author_series.append(author.name + " " + author.surname, author_books/books)

            for i in range(len(self.author_series)):
                slice = QPieSlice()
                slice = self.author_series.slices()[i]
                slice.setLabelVisible(True)
        
        except ZeroDivisionError:
            openDialog(QMessageBox.Critical, 'Insufficient data for chart', 'Error')
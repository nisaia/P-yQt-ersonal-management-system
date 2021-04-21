import sys

from ui.statistics_window import *
from PyQt5.QtWidgets import QWidget
from database.db import session
from database.models import *
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QPainter

class StatisticsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_statistics_window()
        self.ui.setupUi(self)

        self.category_series = QPieSeries()
        self.author_series = QPieSeries()

        self.createChart('Book percentages category', self.category_series)
        self.createChart('Book percentages author', self.author_series)

        self.show()

    def getValues(self):
        books = session.query(Book).count()
        authors = session.query(Author).count()
        categories = session.query(Category).count()

        self.ui.books_counter_label.setText(str(books))
        self.ui.authors_counter_label.setText(str(authors))
        self.ui.categories_counter_label.setText(str(categories))
        

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
        books = session.query(Book).count()

        categories = session.query(Category).all()
        self.category_series.clear()
        for category in categories:
            category_books = session.query(Book).filter_by(category_id=category.id).count()
            self.category_series.append(category.name, category_books/books)

        for i in range(len(self.category_series)):
            slice = QPieSlice()
            slice = self.category_series.slices()[i]
            slice.setLabelVisible(True)

        authors = session.query(Author).all()
        self.author_series.clear()
        for author in authors:
            author_books = session.query(Book).filter_by(author_id=author.id).count()
            self.author_series.append(author.name + " " + author.surname, author_books/books)

        for i in range(len(self.author_series)):
            slice = QPieSlice()
            slice = self.author_series.slices()[i]
            slice.setLabelVisible(True)
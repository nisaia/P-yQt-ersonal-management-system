import sys

from assets.ui_PY.statistics_window import *
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

        self.createChart()

        self.show()

    def getValues(self):
        books = session.query(Book).count()
        authors = session.query(Author).count()
        categories = session.query(Category).count()

        self.ui.books_counter_label.setText(str(books))
        self.ui.authors_counter_label.setText(str(authors))
        self.ui.categories_counter_label.setText(str(categories))
        

    def createChart(self):
        self.series = QPieSeries()

        chart = QChart()
        chart.addSeries(self.series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle('Book categories percentages')

            #sslice.setLabel("{:.1f}%".format(100 * slice.percentage()))

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        #setChart(chartview)
        self.ui.horizontalLayout.addWidget(chartview)

    def updateValues(self):
        self.series.clear()
        books = session.query(Book).count()
        categories = session.query(Category).all()

        for category in categories:
            category_books = session.query(Book).filter_by(category_id=category.id).count()
            self.series.append(category.name, category_books/books)

        for i in range(len(self.series)):
            slice = QPieSlice()
            slice = self.series.slices()[i]
            slice.setLabelVisible(True)
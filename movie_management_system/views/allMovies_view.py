import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from movie_management_system.ui.allMovies_window import *
from database.db import movie_session
from database.movie_models import *

class AllMoviesView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allMovies_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Title', 'Film director', 'Genre']

        self.ui.allMovies_tableView.clicked.connect(self.movie_details)

        self.show()

    def movie_details(self):
        print("GOD")
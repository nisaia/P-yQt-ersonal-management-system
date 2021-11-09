import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from movie_management_system.ui.allFilmDirectors_window import *
from database.db import movie_session
from database.movie_models import *


class AllFilmDirectorsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allFilmDirectors_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Name', 'Surname']
        self.ui.allFilmDirectors_tableView.clicked.connect(self.filmDirector_details)

        self.show()

    def loadData(self):
        filmDirectors = movie_session.query(Film_director).all()
        self.model = QStandardItemModel(len(filmDirectors), len(self.labels))
        self.model.setHorizontalHeaderLabels(self.labels)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)

        for row, filmDirector in enumerate(filmDirectors):
            filmDirector_id = QStandardItem(str(filmDirector.id))
            filmDirector_id.setTextAlignment(Qt.AlignCenter)
            filmDirector_name = QStandardItem(filmDirector.name)
            filmDirector_name.setTextAlignment(Qt.AlignCenter)
            filmDirector_surname = QStandardItem(filmDirector.surname)
            filmDirector_surname.setTextAlignment(Qt.AlignCenter)

            self.model.setItem(row, 0, filmDirector_id)
            self.model.setItem(row, 1, filmDirector_name)
            self.model.setItem(row, 2, filmDirector_surname)

        self.ui.allFilmDirectors_tableView.setModel(self.filter_proxy_model)
        self.ui.allFilmDirectors_tableView.setColumnHidden(0, True)

        self.ui.searchFilmDirector_lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def filmDirector_details(self): pass
import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from movie_management_system.ui.allMovies_window import *
from database.db import movie_session
from database.movie_models import *
from utils.functions import getColorStatus

class AllMoviesView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allMovies_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Title', 'Film director', 'Genre', 'Status']

        self.ui.allMovies_tableView.clicked.connect(self.movie_details)

        self.show()

    def loadData(self):
        results = movie_session.query(Movie, Film_director, Genre, MovieStatus).select_from(Movie).join(Film_director).join(Genre).join(MovieStatus).all()
        self.model = QStandardItemModel(len(results), len(self.labels))
        self.model.setHorizontalHeaderLabels(self.labels)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)

        for row, (movie, film_director, genre, movie_status) in enumerate(results):
            movie_id = QStandardItem(str(movie.id))
            movie_id.setTextAlignment(Qt.AlignCenter)
            movie_title = QStandardItem(movie.title)
            movie_title.setTextAlignment(Qt.AlignCenter)
            filmDirector = QStandardItem(film_director.name + " " + film_director.surname)
            filmDirector.setTextAlignment(Qt.AlignCenter)
            genreI = QStandardItem(genre.name)
            genreI.setTextAlignment(Qt.AlignCenter)
            status = QStandardItem(movie_status.name)
            status.setTextAlignment(Qt.AlignCenter)
            status.setForeground(QBrush(getColorStatus(movie.status_id, movie)))

            self.model.setItem(row, 0, movie_id)
            self.model.setItem(row, 1, movie_title)
            self.model.setItem(row, 2, filmDirector)
            self.model.setItem(row, 3, genreI)
            self.model.setItem(row, 4, status)

        self.ui.allMovies_tableView.setModel(self.filter_proxy_model)
        self.ui.allMovies_tableView.setColumnHidden(0, True)

        self.ui.searchMovie_lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def movie_details(self):
        row = self.ui.allMovies_tableView.selectionModel().selectedRows()[0].row()
        id = self.filter_proxy_model.index(row, 0).data()
        result = movie_session.query(Movie, Film_director, Genre, MovieStatus).select_from(Movie).filter_by(id=id).join(Film_director).join(Genre).join(MovieStatus).first()

        movie, film_director, genre, status = result
        movie_view = self.parent().findChild(QWidget, 'movie_window')
        #movie_view.updateValues(movie, film_director, genre, status)
        self.parent().setCurrentWidget(movie_view)
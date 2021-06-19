import sys
from PyQt5.QtWidgets import QWidget
from database.book_models import Genre
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from book_management_system.ui.allGenres_window import *
from database.db import book_session

class AllGenresView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allGenres_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Name']

        self.ui.allGenres_tableView.clicked.connect(self.editGenre)

        self.show()

    def loadData(self):
        genres = book_session.query(Genre).all()
        self.model = QStandardItemModel(len(genres), len(self.labels))
        self.model.setHorizontalHeaderLabels(self.labels)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)

        for row, genre in enumerate(genres):
            genre_id = QStandardItem(str(genre.id))
            genre_id.setTextAlignment(Qt.AlignCenter)
            genre_name = QStandardItem(genre.name)
            genre_name.setTextAlignment(Qt.AlignCenter)
            self.model.setItem(row, 0, genre_id)
            self.model.setItem(row, 1, genre_name)

        self.ui.allGenres_tableView.setModel(self.filter_proxy_model)
        self.ui.allGenres_tableView.setColumnHidden(0, True)

        self.ui.searchGenre_lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def editGenre(self):
        row = self.ui.allGenres_tableView.selectionModel().selectedRows()[0].row()
        id = self.filter_proxy_model.index(row, 0).data()
        genre = book_session.query(Genre).filter_by(id=id).first()
        genre_view = self.parent().findChild(QWidget, 'genre_window')
        genre_view.updateValues(genre)
        self.parent().setCurrentWidget(genre_view)
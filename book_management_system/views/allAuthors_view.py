import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from book_management_system.ui.allAuthors_window import *
from database.db import book_session
from database.book_models import Author

class AllAuthorsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allAuthors_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Name', 'Surname']

        self.ui.allAuthors_tableView.clicked.connect(self.author_details)

        self.show()

    def loadData(self):
        authors = book_session.query(Author).all()
        self.model = QStandardItemModel(len(authors), len(self.labels))
        self.model.setHorizontalHeaderLabels(self.labels)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)

        for row, author in enumerate(authors):
            author_id = QStandardItem(str(author.id))
            author_id.setTextAlignment(Qt.AlignCenter)
            author_name = QStandardItem(author.name)
            author_name.setTextAlignment(Qt.AlignCenter)
            author_surname = QStandardItem(author.surname)
            author_surname.setTextAlignment(Qt.AlignCenter)

            self.model.setItem(row, 0, author_id)
            self.model.setItem(row, 1, author_name)
            self.model.setItem(row, 2, author_surname)

        self.ui.allAuthors_tableView.setModel(self.filter_proxy_model)
        self.ui.allAuthors_tableView.setColumnHidden(0, True)

        self.ui.searchAuthor_lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def author_details(self):
        row = self.ui.allAuthors_tableView.selectionModel().selectedRows()[0].row()
        id = self.filter_proxy_model.index(row, 0).data()
        author = book_session.query(Author).filter_by(id=id).first()
        author_view = self.parent().findChild(QWidget, 'author_window')
        author_view.updateValues(author)
        self.parent().setCurrentWidget(author_view)
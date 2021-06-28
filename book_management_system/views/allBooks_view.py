import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from book_management_system.ui.allBooks_window import *
from database.db import book_session
from database.book_models import *
from utils.constants import COVER_PATH
from utils.functions import getColorStatus

class AllBooksView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allBooks_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Title', 'ISBN', 'Author', 'Genre', 'Status']

        self.ui.allBooks_tableView.clicked.connect(self.book_details)

        self.show()


    def loadData(self):
        results = book_session.query(Book, Author, Genre).select_from(Book).join(Author).join(Genre).all()
        self.model = QStandardItemModel(len(results), len(self.labels))
        self.model.setHorizontalHeaderLabels(self.labels)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)
        
        for row, (book, author, genre) in enumerate(results):
            book_id = QStandardItem(str(book.id))
            book_id.setTextAlignment(Qt.AlignCenter)
            book_title = QStandardItem(book.title)
            book_title.setTextAlignment(Qt.AlignCenter)
            book_isbn = QStandardItem(book.isbn)
            book_isbn.setTextAlignment(Qt.AlignCenter)
            authorI = QStandardItem(author.name + " " + author.surname)
            authorI.setTextAlignment(Qt.AlignCenter)
            genreI = QStandardItem(genre.name)
            genreI.setTextAlignment(Qt.AlignCenter)
            status = QStandardItem(book.status)
            status.setTextAlignment(Qt.AlignCenter)
            status.setForeground(QBrush(getColorStatus(book.status)))
            
            self.model.setItem(row, 0, book_id)
            self.model.setItem(row, 1, book_title)
            self.model.setItem(row, 2, book_isbn)
            self.model.setItem(row, 3, authorI)
            self.model.setItem(row, 4, genreI)
            self.model.setItem(row, 5, status)

        self.ui.allBooks_tableView.setModel(self.filter_proxy_model)
        self.ui.allBooks_tableView.setColumnHidden(0, True)

        self.ui.searchBook_lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def book_details(self):
        row = self.ui.allBooks_tableView.selectionModel().selectedRows()[0].row()
        id = self.filter_proxy_model.index(row, 0).data()
        result = book_session.query(Book, Author, Genre).select_from(Book).filter_by(id=id).join(Author).join(Genre).first()

        book, author, genre = result
        print(book.id, author.id, genre.id)
        book_view = self.parent().findChild(QWidget, 'book_window')
        book_view.updateValues(book, author, genre)
        self.parent().setCurrentWidget(book_view)
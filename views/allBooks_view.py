import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.allBooks_window import *
from database.db import session
from database.models import *
from views.book_view import BookView

class AllBooksView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_allBooks_window()
        self.ui.setupUi(self)

        self.labels = ['Id', 'Title', 'ISBN', 'Author', 'Genre']

        self.ui.tableView.clicked.connect(self.book_details)

        self.show()


    def loadData(self):
        results = session.query(Book, Author, Genre).select_from(Book).join(Author).join(Genre).all()
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
            self.model.setItem(row, 0, book_id)
            self.model.setItem(row, 1, book_title)
            self.model.setItem(row, 2, book_isbn)
            self.model.setItem(row, 3, authorI)
            self.model.setItem(row, 4, genreI)

        self.ui.tableView.setModel(self.filter_proxy_model)

        self.ui.lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)

    def book_details(self):
        row = self.ui.tableView.selectionModel().selectedRows()[0].row()
        id = self.filter_proxy_model.index(row, 0).data()
        result = session.query(Book, Author, Genre).select_from(Book).filter_by(id=id).join(Author).join(Genre).first()

        book, author, genre = result
        print(book.id, author.id, genre.id)
        book_view = self.parent().findChild(QWidget, 'book_window')
        book_view.updateValues(book, author, genre)
        self.parent().setCurrentWidget(book_view)
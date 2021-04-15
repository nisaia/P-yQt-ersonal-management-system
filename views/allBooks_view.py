import sys
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from assets.ui_PY.allBooks_window import *
from database.db import session
from database.models import *

class AllBooksView(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.loadData()

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.setSourceModel(self.model)
        
        self.ui.tableView.setModel(self.filter_proxy_model)

        self.ui.lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        

        self.show()

    def loadData(self):
        labels = ['Id', 'Title', 'ISBN', 'Author', 'Category']
        results = session.query(Book, Author, Category).select_from(Book).join(Author).join(Category).all()
        print(len(results))
        self.model = QStandardItemModel(len(results), len(labels))
        self.model.setHorizontalHeaderLabels(labels)
        
        for row, (book, author, category) in enumerate(results):
            book_id = QStandardItem(str(book.id))
            book_title = QStandardItem(book.title)
            book_isbn = QStandardItem(book.isbn)
            authorI = QStandardItem(author.name + " " + author.surname)
            categoryI = QStandardItem(category.name)
            self.model.setItem(row, 0, book_id)
            self.model.setItem(row, 1, book_title)
            self.model.setItem(row, 2, book_isbn)
            self.model.setItem(row, 3, authorI)
            self.model.setItem(row, 4, categoryI)

    def reloadTable(self):
        self.loadData()
import sys

from assets.ui_PY.main_window import *
from PyQt5.QtWidgets import QMainWindow
from views.addBook_view import AddBookView
from views.addAuthor_view import AddAuthorView
from views.addCategory_view import AddCategoryView
from views.home_view import HomeView
from views.allBooks_view import AllBooksView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_view = HomeView()
        self.addBook_view = AddBookView()
        self.allBooks_view = AllBooksView()
        self.addAuthor_view = AddAuthorView()
        self.addCategory_view = AddCategoryView()

        self.ui.stackedWidget.addWidget(self.home_view)
        self.ui.stackedWidget.addWidget(self.addBook_view)
        self.ui.stackedWidget.addWidget(self.allBooks_view)
        self.ui.stackedWidget.addWidget(self.addAuthor_view)
        self.ui.stackedWidget.addWidget(self.addCategory_view)
    
        self.ui.home_button.clicked.connect(self.home)
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.allBooks_button.clicked.connect(self.allBooks)
        self.ui.addAuthor_button.clicked.connect(self.addAuthor)
        self.ui.addCategory_button.clicked.connect(self.addCategory)

        self.show()

    def home(self): self.ui.stackedWidget.setCurrentWidget(self.home_view)
    def addBook(self):
        self.addBook_view.update()
        self.ui.stackedWidget.setCurrentWidget(self.addBook_view)

    def allBooks(self):
        self.allBooks_view.reloadTable()
        self.ui.stackedWidget.setCurrentWidget(self.allBooks_view)
    def addAuthor(self): self.ui.stackedWidget.setCurrentWidget(self.addAuthor_view)
    def addCategory(self): self.ui.stackedWidget.setCurrentWidget(self.addCategory_view)
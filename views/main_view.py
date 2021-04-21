import sys

from ui.main_window import *
from PyQt5.QtWidgets import QMainWindow
from views.addBook_view import AddBookView
from views.addAuthor_view import AddAuthorView
from views.addCategory_view import AddCategoryView
from views.home_view import HomeView
from views.allBooks_view import AllBooksView
from views.book_view import BookView
from views.statistics_view import StatisticsView
from views.settings_view import SettingsView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_view = HomeView(parent=self)
        self.addBook_view = AddBookView(parent=self)
        self.allBooks_view = AllBooksView(parent=self)
        self.addAuthor_view = AddAuthorView(parent=self)
        self.addCategory_view = AddCategoryView(parent=self)
        self.book_view = BookView(parent=self)
        self.statistics_view = StatisticsView(parent=self)
        self.settings_view = SettingsView(parent=self)

        self.ui.stackedWidget.addWidget(self.home_view)
        self.ui.stackedWidget.addWidget(self.addBook_view)
        self.ui.stackedWidget.addWidget(self.allBooks_view)
        self.ui.stackedWidget.addWidget(self.addAuthor_view)
        self.ui.stackedWidget.addWidget(self.addCategory_view)
        self.ui.stackedWidget.addWidget(self.book_view)
        self.ui.stackedWidget.addWidget(self.statistics_view)
        self.ui.stackedWidget.addWidget(self.settings_view)
    
        self.ui.home_button.clicked.connect(self.home)
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.allBooks_button.clicked.connect(self.allBooks)
        self.ui.addAuthor_button.clicked.connect(self.addAuthor)
        self.ui.addCategory_button.clicked.connect(self.addCategory)
        self.ui.statistics_button.clicked.connect(self.getStatistics)
        self.ui.settings_button.clicked.connect(self.settings)

        self.show()

    def home(self): self.ui.stackedWidget.setCurrentWidget(self.home_view)
    def addBook(self):
        self.addBook_view.update()
        self.ui.stackedWidget.setCurrentWidget(self.addBook_view)
        print(self.ui.stackedWidget.count())
        print(self.addBook_view.parent())

    def allBooks(self):
        self.allBooks_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allBooks_view)
    def addAuthor(self): self.ui.stackedWidget.setCurrentWidget(self.addAuthor_view)
    def addCategory(self): self.ui.stackedWidget.setCurrentWidget(self.addCategory_view)
    def getStatistics(self):
        self.statistics_view.getValues()
        self.statistics_view.updateValues()
        self.ui.stackedWidget.setCurrentWidget(self.statistics_view)
        #app = QtWidgets.QApplication.instance()

    def settings(self):
        self.settings_view.updateStyles()
        self.ui.stackedWidget.setCurrentWidget(self.settings_view)
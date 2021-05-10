import sys

from ui.main_window import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from views.addBook_view import AddBookView
from views.addAuthor_view import AddAuthorView
from views.addGenre_view import AddGenreView
from views.home_view import HomeView
from views.allBooks_view import AllBooksView
from views.book_view import BookView
from views.statistics_view import StatisticsView
from views.settings_view import SettingsView
from views.allAuthors_view import AllAuthorsView
from views.author_view import AuthorView
from views.allGenres_view import AllGenresView
from views.genre_view import GenreView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_view = HomeView(parent=self)
        self.addBook_view = AddBookView(parent=self)
        self.allBooks_view = AllBooksView(parent=self)
        self.book_view = BookView(parent=self)
        self.addAuthor_view = AddAuthorView(parent=self)
        self.allAuthors_view = AllAuthorsView(parent=self)
        self.author_view = AuthorView(parent=self)
        self.addGenre_view = AddGenreView(parent=self)
        self.allGenres_view = AllGenresView(parent=self)
        self.genre_view = GenreView(parent=self)
        self.statistics_view = StatisticsView(parent=self)
        self.settings_view = SettingsView(parent=self)

        self.ui.stackedWidget.addWidget(self.home_view)
        self.ui.stackedWidget.addWidget(self.addBook_view)
        self.ui.stackedWidget.addWidget(self.allBooks_view)
        self.ui.stackedWidget.addWidget(self.book_view)
        self.ui.stackedWidget.addWidget(self.addAuthor_view)
        self.ui.stackedWidget.addWidget(self.allAuthors_view)
        self.ui.stackedWidget.addWidget(self.author_view)
        self.ui.stackedWidget.addWidget(self.addGenre_view)
        self.ui.stackedWidget.addWidget(self.allGenres_view)
        self.ui.stackedWidget.addWidget(self.genre_view)
        self.ui.stackedWidget.addWidget(self.statistics_view)
        self.ui.stackedWidget.addWidget(self.settings_view)
    
        self.ui.home_button.clicked.connect(self.home)
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.allBooks_button.clicked.connect(self.allBooks)
        self.ui.addAuthor_button.clicked.connect(self.addAuthor)
        self.ui.allAuthors_button.clicked.connect(self.allAuthors)
        self.ui.addGenre_button.clicked.connect(self.addGenre)
        self.ui.allGenres_button.clicked.connect(self.allGenres)
        self.ui.statistics_button.clicked.connect(self.getStatistics)
        self.ui.settings_button.clicked.connect(self.changeSettings)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.show()

    def home(self):
        print(self.home_view)
        self.ui.stackedWidget.setCurrentWidget(self.home_view)
    
    def addBook(self):
        self.addBook_view.updateComboBox()
        self.ui.stackedWidget.setCurrentWidget(self.addBook_view)
        print(self.ui.stackedWidget.count())
        print(self.addBook_view.parent())

    def allBooks(self):
        self.allBooks_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allBooks_view)
    
    def addAuthor(self): self.ui.stackedWidget.setCurrentWidget(self.addAuthor_view)
    
    def allAuthors(self):
        self.allAuthors_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allAuthors_view)
    
    def addGenre(self): self.ui.stackedWidget.setCurrentWidget(self.addGenre_view)

    def allGenres(self):
        self.allGenres_view.loadData()
        self.ui.stackedWidget.setCurrentWidget(self.allGenres_view)
    
    def getStatistics(self):
        self.statistics_view.getValues()
        self.statistics_view.updateValues()
        self.ui.stackedWidget.setCurrentWidget(self.statistics_view)

    def changeSettings(self):
        self.settings_view.updateValues()
        self.ui.stackedWidget.setCurrentWidget(self.settings_view)
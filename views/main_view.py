import sys

from assets.ui_PY.main_window import *
from PyQt5.QtWidgets import QMainWindow
from views.addBook_view import AddBookView
from views.addAuthor_view import AddAuthorView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.addBook_view = AddBookView()
        self.addAuthor_view = AddAuthorView()

        self.ui.stackedWidget.addWidget(self.addBook_view)
        self.ui.stackedWidget.addWidget(self.addAuthor_view)
    
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.addAuthor_button.clicked.connect(self.addAuthor)

        self.show()

    def addBook(self): self.ui.stackedWidget.setCurrentWidget(self.addBook_view)
    def addAuthor(self): self.ui.stackedWidget.setCurrentWidget(self.addAuthor_view)

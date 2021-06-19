import sys

from ui.main_window import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from book_management_system.views.main_view import BookMainView

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.book_main_view = BookMainView(parent=self)

        self.ui.stackedWidget.addWidget(self.book_main_view)

        #self.movie_main_view = MovieMainView(parent=self)
        #self.music_main_view = MusicMainView(parent=self)

        self.ui.bookManagementSystem_button.clicked.connect(self.book_management_system)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()

    def book_management_system(self):
        self.ui.stackedWidget.setCurrentWidget(self.book_main_view)
        #print(self.ui.stackedWidget.count())
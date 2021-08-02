import sys

from ui.main_window import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from book_management_system.views.main_view import BookMainView
from movie_management_system.views.main_view import MovieMainView
from views.settings_view import SettingsView
from utils.constants import IMAGES_PATH
from os.path import join
from PyQt5.QtGui import QPixmap

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.book_main_view = BookMainView(parent=self)
        self.movie_main_view = MovieMainView(parent=self)
        #self.music_main_view = MusicMainView(parent=self)

        self.settings_view = SettingsView(parent=self)

        self.ui.stackedWidget.addWidget(self.book_main_view)
        self.ui.stackedWidget.addWidget(self.movie_main_view)

        self.ui.stackedWidget.addWidget(self.settings_view)


        self.ui.bookManagementSystem_button.clicked.connect(self.book_management_system)
        self.ui.movieManagementSystem_button.clicked.connect(self.movie_management_system)

        self.ui.settings_button.clicked.connect(self.changeSettings)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        logo = QPixmap(join(IMAGES_PATH, 'logo_transparent.png'))
        self.ui.logo_label.setPixmap(logo)
        #self.ui.logo_label.setScaledContents(True)

        self.show()

    def book_management_system(self):
        self.ui.stackedWidget.setCurrentWidget(self.book_main_view)

    def movie_management_system(self):
        self.ui.stackedWidget.setCurrentWidget(self.movie_main_view)

    def changeSettings(self):
        self.settings_view.updateValues()
        self.ui.stackedWidget.setCurrentWidget(self.settings_view)

from views.main_view import MainView
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QFont
from utils.constants import BASIC_QT_CLASSES

class GUI(MainView):

    def __init__(self):
        super().__init__()

        #self.main_view = MainView()

        self.settings = QSettings('settings.ini', QSettings.IniFormat)

        #self.main_view.show()
        #self.main_view.setWindowTitle('P(yQt)ersonal book library')

    def loadSettings(self):
        app = QApplication.instance()
        try:
            app.setStyleSheet(self.settings.value('app_style'))
            for _class in BASIC_QT_CLASSES:
                app.setFont(QFont(self.settings.value('app_font')), _class)
        except:
            pass

    def closeEvent(self, event):
        app = QApplication.instance()
        self.settings.setValue('app_style', app.styleSheet())
        self.settings.setValue('app_font', app.font().toString())
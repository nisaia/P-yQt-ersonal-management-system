from views.main_view import MainView
from PyQt5.QtCore import QSettings

class App():

    def __init__(self):
        super().__init__()
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.main_window = MainView()
        self.main_window.setWindowTitle('PyBooks')
        
        try:
            self.main_window.setStyleSheet(self.settings.value('qss'))
        except:
            pass

    def run(self):
        print(QSettings.fileName(self.settings))
        self.main_window.show()

    def closeEvent(self, event):
        print(self.main_window.styleSheet())
        self.settings.setValue('qss', self.main_window.style())
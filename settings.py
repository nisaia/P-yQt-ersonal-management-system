from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication

class Settings():

    def __init__(self):
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def closeEvent(self, event):
        app = QApplication.instance()
        self.settings.setValue('windows_size', app.size())
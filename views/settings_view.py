import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtCore import QTranslator
from ui.settings_window import *
from utils.constants import STYLES_PATH, TRANSLATIONS_PATH, BASIC_QT_CLASSES
from os import listdir
from os.path import isfile, join

class SettingsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_settings_window()
        self.ui.setupUi(self)

        self.ui.changeStyle_button.clicked.connect(self.changeStyle)
        self.ui.changeFont_button.clicked.connect(self.changeFont)
        self.ui.changeLanguage_button.clicked.connect(self.changeLanguage)


        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()
    
    def updateValues(self):
        self.ui.style_comboBox.clear()
        
        for file in listdir(STYLES_PATH):
            self.ui.style_comboBox.addItem(file)

        self.ui.language_comboBox.clear()

        for file in listdir(TRANSLATIONS_PATH):
            self.ui.language_comboBox.addItem(file)

        #CONTINUE

    def changeStyle(self):
        app = QtWidgets.QApplication.instance()
        currentStyle = self.ui.style_comboBox.currentText()
        with open(join(STYLES_PATH, currentStyle), 'r') as f:
            qss = f.read()
            app.setStyleSheet(qss)

    def changeLanguage(self):
        """app = QtWidgets.QApplication.instance()
        translator = QTranslator()
        currentLanguage = self.ui.language_comboBox.currentText()
        app.installTranslator(translator)"""
        pass

    def changeFont(self):
        app = QtWidgets.QApplication.instance()
        currentFont = self.ui.fontComboBox.currentFont()
        for _class in BASIC_QT_CLASSES:
            app.setFont(currentFont, _class)
        app.setFont(currentFont)
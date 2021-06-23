import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTranslator
from ui.settings_window import *
from utils.constants import STYLES_PATH, TRANSLATIONS_PATH, BASIC_QT_CLASSES, FLAGS_PATH
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

        self.languages_dict = {
            'Italy': 'it',
            'UK': 'uk',
            'Spain': 'es'
        }

        self.translator = QTranslator()

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()
    
    def updateValues(self):
        self.ui.applicationStyle_comboBox.clear()
        
        self.ui.applicationStyle_comboBox.addItem("No style")
        for file in listdir(STYLES_PATH):
            self.ui.applicationStyle_comboBox.addItem(file)

        self.ui.applicationLanguage_comboBox.clear()

        for lang in self.languages_dict:
            self.ui.applicationLanguage_comboBox.addItem(QIcon(join(FLAGS_PATH, self.languages_dict[lang]+'.png')), lang)


        #CONTINUE

    def changeStyle(self):
        app = QtWidgets.QApplication.instance()
        currentStyle = self.ui.applicationStyle_comboBox.currentText()
        if currentStyle == "No style": app.setStyleSheet("")
        else:
            with open(join(STYLES_PATH, currentStyle), 'r') as f:
                qss = f.read()
                app.setStyleSheet(qss)

    def changeLanguage(self):
        app = QtWidgets.QApplication.instance()
        #translator = QTranslator()
        currentItem = self.ui.applicationLanguage_comboBox.currentText()
        currentLanguage = join(TRANSLATIONS_PATH, self.languages_dict[currentItem] + ".qm")
        print(self.translator.load(currentLanguage))
        app.installTranslator(self.translator)

    def changeFont(self):
        app = QtWidgets.QApplication.instance()
        currentFont = self.ui.applicationFont_comboBox.currentFont()
        for _class in BASIC_QT_CLASSES:
            app.setFont(currentFont, _class)
        app.setFont(currentFont)
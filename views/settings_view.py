import sys

from PyQt5.QtWidgets import QWidget
from assets.ui_PY.settings_window import *
from utils.constants import styles_path
from os import listdir
from os.path import isfile, join

class SettingsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_settings_window()
        self.ui.setupUi(self)

        self.ui.changeStyle_button.clicked.connect(self.changeStyle)

        self.show()
    
    def updateStyles(self):
        self.ui.comboBox.clear()
        
        for file in listdir(styles_path):
            if isfile(join(styles_path, file)):
                self.ui.comboBox.addItem(file)

    def changeStyle(self):
        app = QtWidgets.QApplication.instance()
        currenStyle = self.ui.comboBox.currentText()
        with open(join(styles_path, currenStyle), 'r') as f:
            qss = f.read()
            app.setStyleSheet(qss)

        
                
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from os.path import join
from utils.constants import STYLES_PATH, ICONS_PATH
from gui import GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(join(ICONS_PATH, 'book_window_icon.png')))
    gui = GUI()
    gui.setWindowTitle('P(yQt)ersonal book library')
    gui.loadSettings()
    sys.exit(app.exec_())

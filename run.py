import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from views.main_view import MainView
from os.path import join
from utils.constants import STYLES_PATH, ICONS_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(join(ICONS_PATH, 'book_window_icon.png')))
    with open(join(STYLES_PATH, 'light_minimal.qss'), 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)
    main_window = MainView()
    main_window.setWindowTitle('Personal book library')
    main_window.show()
    sys.exit(app.exec_())
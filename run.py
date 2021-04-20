import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from views.main_view import MainView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open('assets/styles/style.qss', 'r') as f:
        qss = f.read()
        app.setStyleSheet(qss)
    main_window = MainView()
    main_window.show()
    sys.exit(app.exec_())
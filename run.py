import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import *
from database.db import create_database

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    sys.exit(app.exec_())
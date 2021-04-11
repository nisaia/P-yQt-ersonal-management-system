import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoLineEdit import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        self.ui.label.setText("Hello " + self.ui.lineEditName.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
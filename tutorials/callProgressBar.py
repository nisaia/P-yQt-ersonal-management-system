import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoProgressBar import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonStartProgressBar.clicked.connect(self.updateProgressBar)

        self.show()

    def updateProgressBar(self):
        x = 0
        while x < 100:
            x+= 0.00001
            self.ui.progressBar.setValue(x)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
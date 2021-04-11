import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoLineEdit import *

class Student:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonClickMe.clicked.connect(self.dispMessage)
        self.show()

    def dispMessage(self):
        student = Student(self.ui.lineEditName.text())
        self.ui.label.setText("Hello " + student.getName())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
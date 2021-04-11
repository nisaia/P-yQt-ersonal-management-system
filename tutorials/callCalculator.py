import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoCalculator import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonAdd.clicked.connect(self.addition)
        self.ui.pushButtonSub.clicked.connect(self.subtraction)
        self.ui.pushButtonMul.clicked.connect(self.multiplication)
        self.ui.pushButtonDiv.clicked.connect(self.division)

        self.show()

    def addition(self):

        if len(self.ui.lineEditFirstNumber.text()) == 0: first_number = 0
        else: first_number = self.ui.lineEditFirstNumber.text()

        if len(self.ui.lineEditSecondNumber.text()) == 0: second_number = 0
        else: second_number = self.ui.lineEditSecondNumber.text()

        
        self.ui.labelResult.setText("Result: " + str((int(first_number) + int(second_number))))

    def subtraction(self):
        if len(self.ui.lineEditFirstNumber.text()) == 0: first_number = 0
        else: first_number = self.ui.lineEditFirstNumber.text()

        if len(self.ui.lineEditSecondNumber.text()) == 0: second_number = 0
        else: second_number = self.ui.lineEditSecondNumber.text()

        
        self.ui.labelResult.setText("Result: " + str((int(first_number) - int(second_number))))


    def multiplication(self):
        if len(self.ui.lineEditFirstNumber.text()) == 0: first_number = 0
        else: first_number = self.ui.lineEditFirstNumber.text()

        if len(self.ui.lineEditSecondNumber.text()) == 0: second_number = 0
        else: second_number = self.ui.lineEditSecondNumber.text()

        
        self.ui.labelResult.setText("Result: " + str((int(first_number) * int(second_number))))

    def division(self):
        if len(self.ui.lineEditFirstNumber.text()) == 0: first_number = 0
        else: first_number = self.ui.lineEditFirstNumber.text()

        if len(self.ui.lineEditSecondNumber.text()) == 0:
            self.ui.labelResult.setText("Cannot divide for zero. Choose another number")
        else:
            second_number = self.ui.lineEditSecondNumber.text()
            self.ui.labelResult.setText("Result: " + str((int(first_number) / int(second_number))))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())

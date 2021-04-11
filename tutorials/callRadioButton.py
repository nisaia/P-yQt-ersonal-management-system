import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoRadioButton import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked():
            fare = 150
        elif self.ui.radioButtonBusinessClass.isChecked():
            fare = 125
        elif self.ui.radioButtonEconomyClass.isChecked():
            fare = 100
        self.ui.labelFare.setText("Air Fare is: " + str(fare))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
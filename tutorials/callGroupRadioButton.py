import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoGroupRadioButton import *

class MyForm(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioButtonM.toggled.connect(self.dispSelected)
        self.ui.radioButtonL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)

        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)

        self.show()

    def dispSelected(self):
        size = ""
        payment = ""

        if self.ui.radioButtonM.isChecked(): size = "Medium"
        elif self.ui.radioButtonL.isChecked(): size = "Large"
        elif self.ui.radioButtonXL.isChecked(): size = "Extra Large"
        elif self.ui.radioButtonXXL.isChecked(): size = "Extra Extra Large"

        if self.ui.radioButtonDebitCard.isChecked(): payment = "Debit/Credit card"
        elif self.ui.radioButtonNetBanking.isChecked(): payment = "Net banking"
        elif self.ui.radioButtonCashOnDelivery.isChecked(): payment = "Cash on delivery"

        if size and payment:
            self.ui.labelSelected.setText("Shirt size: " + size + "\nPayment method: " + payment)
        else:
            if size and not payment:
                self.ui.labelSelected.setText("Chosen shirt size. Choose method payment.")
            elif payment and not size:
                self.ui.labelSelected.setText("Chosen method payment. Choose shirt size.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
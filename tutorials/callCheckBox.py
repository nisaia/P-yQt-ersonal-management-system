import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from views.demoCheckBox import *

class MyForm(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausages.stateChanged.connect(self.dispAmount)

        self.show()
    
    def dispAmount(self):
        default_amount = 10
        
        if self.ui.checkBoxCheese.isChecked(): default_amount += 1
        if self.ui.checkBoxOlives.isChecked(): default_amount += 1
        if self.ui.checkBoxSausages.isChecked(): default_amount += 2

        self.ui.labelAmount.setText("Total amount for pizza is: " + str(default_amount))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
        
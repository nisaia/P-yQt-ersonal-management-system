import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoMultipleListWidget import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.listWidgetDiagnosis.itemSelectionChanged.connect(self.dispSelectedTest)

        self.show()

    def dispSelectedTest(self):
        self.ui.listWidgetSelectedTest.clear()
        items = self.ui.listWidgetDiagnosis.selectedItems()
        for item in items:
            self.ui.listWidgetSelectedTest.addItem(item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
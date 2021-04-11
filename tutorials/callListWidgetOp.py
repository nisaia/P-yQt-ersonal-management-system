import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox
from views.demoListWidgetOp import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.listWidgetSelectedItems.addItem('Ice cream')
        self.ui.listWidgetSelectedItems.addItem('Soda')
        self.ui.listWidgetSelectedItems.addItem('Coffee')
        self.ui.listWidgetSelectedItems.addItem('Chocolate')
        
        self.ui.pushButtonAddItem.clicked.connect(self.addItem)
        self.ui.pushButtonEditItem.clicked.connect(self.editList)
        self.ui.pushButtonDeleteItem.clicked.connect(self.deleteItem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.deleteAll)

        self.show()

    def addItem(self):
        self.ui.listWidgetSelectedItems.addItem(self.ui.lineEditItem.text())
        self.ui.lineEditItem.setText('')
        self.ui.lineEditItem.setFocus()

    def editList(self):
        row = self.ui.listWidgetSelectedItems.currentRow()
        newText, ok=QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and len(newText) != 0:
            self.ui.listWidgetSelectedItems.takeItem(row)
            self.ui.listWidgetSelectedItems.insertItem(row, QListWidgetItem(newText))

    def deleteItem(self):
        ok = QMessageBox().question(self,'Message', 'Are you sure to delete the item?', QMessageBox.Yes, QMessageBox.No)
        if ok == QMessageBox.Yes:
            self.ui.listWidgetSelectedItems.takeItem(self.ui.listWidgetSelectedItems.currentRow())

    def deleteAll(self):
        ok = QMessageBox().question(self,'Message', 'Are you sure to delete all items?', QMessageBox.Yes, QMessageBox.No)
        if ok == QMessageBox.Yes:
            self.ui.listWidgetSelectedItems.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
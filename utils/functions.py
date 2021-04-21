from PyQt5.QtWidgets import QMessageBox

def openDialog(icon, text, title):
    box = QMessageBox()
    box.setIcon(icon)
    box.setText(text)
    box.setWindowTitle(title)
    box.exec_()
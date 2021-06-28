from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor

def openDialog(icon, text, title):
    box = QMessageBox()
    box.setIcon(icon)
    box.setText(text)
    box.setWindowTitle(title)
    box.exec_()

def getColorStatus(status):
    if status == 'Not completed': color = QColor(255, 0, 0)
    elif status == 'In progress': color = QColor(0, 0, 255)
    elif status == 'Completed': color = QColor(0, 100, 0)
    return color
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor
from database.book_models import Status
from database.db import book_session

def openDialog(icon, text, title):
    box = QMessageBox()
    box.setIcon(icon)
    box.setText(text)
    box.setWindowTitle(title)
    box.exec_()

def getColorStatus(status_id):

    #MOLTO PIÙ STRUTTURATO RISPETTO A DEI SEMPLICI CONTROLLI CON I NUMERI

    status_dict = {
        'Not completed': QColor(255, 0, 0),
        'In progress' : QColor(0, 0, 255),
        'Completed': QColor(0, 100, 0)
    }
    all_status = book_session.query(Status).all()

    for status in all_status:
        if status.id == status_id:
            return status_dict[status.name]
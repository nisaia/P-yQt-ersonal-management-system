from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QColor, QPixmap
from database.book_models import Book, BookStatus
from database.movie_models import Movie, MovieStatus

from database.db import book_session, movie_session
from book_management_system.views.coverIllustration_view import CoverIllustrationView

def openDialog(icon, text, title):
    box = QMessageBox()
    box.setIcon(icon)
    box.setText(text)
    box.setWindowTitle(title)
    box.exec_()

def getColorStatus(status_id, model):

    #MOLTO PIÙ STRUTTURATO RISPETTO A DEI SEMPLICI CONTROLLI CON I NUMERI

    status_dict = {
        'Not readed': QColor(255, 0, 0),
        'In progress' : QColor(0, 0, 255),
        'Readed': QColor(0, 100, 0),
        'Not watched': QColor(255, 0, 0),
        'Watched': QColor(0, 100, 0)
    }
    if isinstance(model, Book): all_status = book_session.query(BookStatus).all()
    else: all_status = movie_session.query(MovieStatus).all()

    for status in all_status:
        if status.id == status_id:
            return status_dict[status.name]

def displayCover(label):
        coverIllustration_window = CoverIllustrationView()
        coverIllustration_window.setModal(True)
        
        image = QPixmap(label.text())
        image = image.scaled(coverIllustration_window.ui.coverIllustration_label.width(), coverIllustration_window.ui.coverIllustration_label.height(), QtCore.Qt.KeepAspectRatio)
        coverIllustration_window.ui.coverIllustration_label.setPixmap(image)
        coverIllustration_window.ui.coverIllustration_label.setScaledContents(True)

        coverIllustration_window.exec_()

def get_image_file(parent, label, button):
        file_name, _ = QFileDialog.getOpenFileName(parent, 'Open image file', r"/", "Image files (*.jpg *.png)")
        if len(file_name) != 0:
            label.setText(file_name)
            label.setVisible(True)
            button.setVisible(True)
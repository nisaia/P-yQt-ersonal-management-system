from PyQt5.QtWidgets import QMessageBox

class Error(Exception):
    """Base class for other exceptions"""


class NoInputException(Error):
    """Raised when length of the input value is 0"""
    
    def __init__(self, error_message):
        self.error_message = error_message

    def showMessage(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText(self.error_message)
        error_box.setWindowTitle('Error')
        error_box.exec_()
from PyQt5.QtWidgets import QMessageBox

class Error(Exception):
    """Base class for other exceptions"""


class NoInputException(Error):
    """Raised when length of the input value is 0"""
    
    def __init__(self, error_message):
        self.error_message = error_message
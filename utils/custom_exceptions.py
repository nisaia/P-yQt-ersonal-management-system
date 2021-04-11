class Error(Exception):
    """Base class for other exceptions"""


class NoInputException(Error):
    """Raised when length of the input value is 0"""
    pass
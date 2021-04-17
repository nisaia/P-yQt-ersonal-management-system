import sys
from PyQt5.QtWidgets import QWidget
from assets.ui_PY.book_window import *
from PyQt5.QtGui import QPixmap
from database.models import *
from database.db import session

class BookView(QWidget):

    def __init__(self, parent, book, author, category):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # FIRST TAB
        self.ui.title.setText(book.title)
        self.ui.isbn.setText(book.isbn)
        image = QPixmap(book.image_path)
        image = image.scaled(self.ui.cover.width(), self.ui.cover.height(), QtCore.Qt.KeepAspectRatio)
        self.ui.cover.setPixmap(image)
        self.ui.author.setText(author.name + " " + author.surname)
        self.ui.category.setText(category.name)
        self.ui.description.setText(book.description)

        #SECOND TAB
        self.ui.bookTitle_lineEdit.setText(book.title)
        self.ui.isbn_lineEdit.setText(book.isbn)
        self.ui.coverPath_label.setText(book.image_path)
        self.ui.description_plainTextEdit.setPlainText(book.description)

        self.ui.editBook_button.clicked.connect(self.editBook)
        self.ui.clearAll_button.clicked.connect(self.clearAll)
        #self.ui.deleteBook_button.clicked.connect(self.deleteBook)

        self.show()

    def update(self):
        self.ui.author_comboBox.clear()
        self.ui.category_comboBox.clear()

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.author_comboBox.addItem('No authors founded')
            self.ui.author_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.author_comboBox.addItem(str(author.name + " " + author.surname))
            self.ui.author_comboBox.setDisabled(False)

        categories = session.query(Category).all()
        if len(categories) == 0:
            self.ui.category_comboBox.addItem('No categories founded')
            self.ui.category_comboBox.setDisabled(True)
        else:
            for category in categories:
                self.ui.category_comboBox.addItem(category.name)
            self.ui.category_comboBox.setDisabled(False)

        def editBook(self): pass

        def clearAll(self): pass

        def deleteBook(self): pass
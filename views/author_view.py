import sys
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from ui.author_window import *
from database.models import Author, Book
from database.db import session
from utils.custom_exceptions import *
from utils.functions import openDialog


class AuthorView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_author_window()
        self.ui.setupUi(self)

        self.ui.editAuthor_button.clicked.connect(self.editAuthor)
        self.ui.deleteAuthor_button.clicked.connect(self.deleteAuthor)

        self.findChild(QtWidgets.QTabWidget).tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        self.show()

    def updateValues(self, author):
        self.author = author

        #FIRST TAB
        self.ui.authorName_label.setText(self.author.name)
        self.ui.authorSurname_label.setText(self.author.surname)

        linkTemplate = '<a href={0}>{1}</a>'
        wikipedia_header = 'https://it.wikipedia.org/wiki/'
        author_url = self.author.name + '_' + self.author.surname

        self.ui.authorWikipedia_label.setText(linkTemplate.format(wikipedia_header + author_url, author_url.replace('_', ' ')))

        #SECOND TAB
        self.ui.authorName_lineEdit.setText(self.author.name)
        self.ui.authorSurname_lineEdit.setText(self.author.surname)

    def editAuthor(self):
        try:
            name = self.ui.authorName_lineEdit.text()
            surname = self.ui.authorSurname_lineEdit.text()

            if len(name) == 0: raise NoInputException('Enter name of the author')
            elif len(surname) == 0: raise NoInputException('Enter surname of the author')

            if self.author.name != name or self.author.surname != surname:
                updates = {
                    'name': name,
                    'surname': surname
                }

                for key, value in updates.items():
                    setattr(self.author, key, value)
                
                session.commit()
                openDialog(QMessageBox.Information, 'Author edited', 'Success')
            else:
                openDialog(QMessageBox.Information, 'Nothing changed', 'Success')
            
            home_window = self.parent().findChild(QWidget, 'home_window')
            self.parent().setCurrentWidget(home_window)


        except NoInputException as e:
            message = e.error_message
            openDialog(QMessageBox.Critical, message, 'Error')

    def deleteAuthor(self):
        
        #CANCELLO TUTTI I LIBRI ASSOCIATI ALL'AUTORE
        books = session.query(Book).filter_by(author_id=self.author.id).all()

        for book in books:
            session.delete(book)

        session.delete(self.author)

        session.commit()
        home_window = self.parent().findChild(QWidget, 'home_window')
        self.parent().setCurrentWidget(home_window)

        openDialog(QMessageBox.Information, 'Author deleted', 'Success')
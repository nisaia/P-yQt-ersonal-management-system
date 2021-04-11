import sys
from PyQt5.QtWidgets import QWidget, QFileDialog
from assets.ui_PY.addBook_window import *
from database.db import session
from database.models import Author, Category, Book
from PyQt5.QtGui import QPixmap

class AddBookView(QWidget):
    
    def __init__(self):

        self.cover_path = ""

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        authors = session.query(Author).all()
        if len(authors) == 0:
            self.ui.author_comboBox.addItem('No authors founded')
            self.ui.author_comboBox.setDisabled(True)
        else:
            for author in authors:
                self.ui.author_comboBox.addItem(str(author.name + " " + author.surname))

        categories = session.query(Category).all()
        if len(categories) == 0:
            self.ui.category_comboBox.addItem('No categories founded')
            self.ui.category_comboBox.setDisabled(True)
        else:
            for category in categories:
                self.ui.category_comboBox.addItem(category.name)
        

        self.ui.uploadCover_button.clicked.connect(self.get_image_file)
                
        self.ui.addBook_button.clicked.connect(self.addBook)
        self.ui.clearAll_button.clicked.connect(self.clearAll)
        
        self.show()

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"/", "Image files (*.jpg *.png)")
        image = QPixmap(file_name)
        self.ui.image_label.setPixmap(image)
        self.cover_path = file_name

    def addBook(self):
        book_title = self.ui.bookTitle_lineEdit.text()
        isbn = self.ui.ISBN_lineEdit.text()
        author = session.query(Author).filter_by(id=self.ui.author_comboBox.currentIndex()+1).first()
        #category = session.query(Category).filter_by(id=self.ui.category_comboBox.currentIndex()).first()
        cover_path = self.cover_path
        description = self.ui.description_plainText.toPlainText()

        book = Book(title=book_title,
                    isbn=isbn,
                    author_id=author.id,
                    category_id=1,
                    description=description,
                    image_path=cover_path)
        
        session.add(book)
        session.commit()

        self.clearAll()


    def clearAll(self):
        self.ui.bookTitle_lineEdit.clear()
        self.ui.ISBN_lineEdit.clear()
        self.ui.author_comboBox.setCurrentIndex(0)
        self.ui.category_comboBox.setCurrentIndex(0)
        self.cover_path = ""
        self.ui.image_label.clear()
        self.ui.description_plainText.clear()
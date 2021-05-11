# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/book_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_book_window(object):
    def setupUi(self, book_window):
        book_window.setObjectName("book_window")
        book_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(book_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(book_window)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.bookIsbn_label = QtWidgets.QLabel(self.tab)
        self.bookIsbn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookIsbn_label.setObjectName("bookIsbn_label")
        self.gridLayout.addWidget(self.bookIsbn_label, 1, 1, 1, 1)
        self.bookGenre_label = QtWidgets.QLabel(self.tab)
        self.bookGenre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookGenre_label.setObjectName("bookGenre_label")
        self.gridLayout.addWidget(self.bookGenre_label, 3, 1, 1, 1)
        self.bookDescription_label = QtWidgets.QLabel(self.tab)
        self.bookDescription_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookDescription_label.setObjectName("bookDescription_label")
        self.gridLayout.addWidget(self.bookDescription_label, 4, 0, 1, 2)
        self.bookTitle_label = QtWidgets.QLabel(self.tab)
        self.bookTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookTitle_label.setObjectName("bookTitle_label")
        self.gridLayout.addWidget(self.bookTitle_label, 0, 1, 1, 1)
        self.bookAuthor_label = QtWidgets.QLabel(self.tab)
        self.bookAuthor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookAuthor_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.bookAuthor_label.setObjectName("bookAuthor_label")
        self.gridLayout.addWidget(self.bookAuthor_label, 2, 1, 1, 1)
        self.bookCover_label = QtWidgets.QLabel(self.tab)
        self.bookCover_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bookCover_label.setObjectName("bookCover_label")
        self.gridLayout.addWidget(self.bookCover_label, 0, 0, 4, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.editBook_label = QtWidgets.QLabel(self.tab_2)
        self.editBook_label.setAlignment(QtCore.Qt.AlignCenter)
        self.editBook_label.setObjectName("editBook_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.editBook_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.bookTitle_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookTitle_label_2.setObjectName("bookTitle_label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookTitle_label_2)
        self.bookTitle_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.bookTitle_lineEdit.setObjectName("bookTitle_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookTitle_lineEdit)
        self.bookIsbn_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookIsbn_label_2.setObjectName("bookIsbn_label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bookIsbn_label_2)
        self.bookIsbn_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.bookIsbn_lineEdit.setObjectName("bookIsbn_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bookIsbn_lineEdit)
        self.bookAuthor_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookAuthor_label_2.setObjectName("bookAuthor_label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.bookAuthor_label_2)
        self.bookAuthor_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.bookAuthor_comboBox.setObjectName("bookAuthor_comboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bookAuthor_comboBox)
        self.bookGenre_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookGenre_label_2.setObjectName("bookGenre_label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.bookGenre_label_2)
        self.bookGenre_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.bookGenre_comboBox.setObjectName("bookGenre_comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bookGenre_comboBox)
        self.bookCover_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookCover_label_2.setObjectName("bookCover_label_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.bookCover_label_2)
        self.bookPreview_button = QtWidgets.QPushButton(self.tab_2)
        self.bookPreview_button.setObjectName("bookPreview_button")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.bookPreview_button)
        self.bookDescription_label_2 = QtWidgets.QLabel(self.tab_2)
        self.bookDescription_label_2.setObjectName("bookDescription_label_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.bookDescription_label_2)
        self.bookDescription_plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.bookDescription_plainTextEdit.setObjectName("bookDescription_plainTextEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.bookDescription_plainTextEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.editBook_button = QtWidgets.QPushButton(self.tab_2)
        self.editBook_button.setObjectName("editBook_button")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.editBook_button)
        self.deleteBook_button = QtWidgets.QPushButton(self.tab_2)
        self.deleteBook_button.setObjectName("deleteBook_button")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.deleteBook_button)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uploadCover_button = QtWidgets.QPushButton(self.tab_2)
        self.uploadCover_button.setObjectName("uploadCover_button")
        self.horizontalLayout.addWidget(self.uploadCover_button)
        self.bookCoverPath_label = QtWidgets.QLabel(self.tab_2)
        self.bookCoverPath_label.setText("")
        self.bookCoverPath_label.setObjectName("bookCoverPath_label")
        self.horizontalLayout.addWidget(self.bookCoverPath_label)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(book_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(book_window)

    def retranslateUi(self, book_window):
        _translate = QtCore.QCoreApplication.translate
        book_window.setWindowTitle(_translate("book_window", "Form"))
        self.bookIsbn_label.setText(_translate("book_window", "ISBN"))
        self.bookGenre_label.setText(_translate("book_window", "Genre"))
        self.bookDescription_label.setText(_translate("book_window", "Description"))
        self.bookTitle_label.setText(_translate("book_window", "Title"))
        self.bookAuthor_label.setText(_translate("book_window", "Author"))
        self.bookCover_label.setText(_translate("book_window", "Cover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("book_window", "Tab 1"))
        self.editBook_label.setText(_translate("book_window", "Edit book"))
        self.bookTitle_label_2.setText(_translate("book_window", "Title:"))
        self.bookIsbn_label_2.setText(_translate("book_window", "ISBN:"))
        self.bookAuthor_label_2.setText(_translate("book_window", "Author:"))
        self.bookGenre_label_2.setText(_translate("book_window", "Genre:"))
        self.bookCover_label_2.setText(_translate("book_window", "Cover:"))
        self.bookPreview_button.setText(_translate("book_window", "Preview"))
        self.bookDescription_label_2.setText(_translate("book_window", "Description:"))
        self.editBook_button.setText(_translate("book_window", "Edit book"))
        self.deleteBook_button.setText(_translate("book_window", "Delete book"))
        self.uploadCover_button.setText(_translate("book_window", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("book_window", "Tab 2"))

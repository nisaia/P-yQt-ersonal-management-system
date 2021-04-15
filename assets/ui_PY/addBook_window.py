# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui_XML/addBook_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 730)
        Form.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(49, 29, 781, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBook_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.addBook_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addBook_label.setIndent(-1)
        self.addBook_label.setObjectName("addBook_label")
        self.horizontalLayout.addWidget(self.addBook_label)
        self.addBook_frame = QtWidgets.QFrame(Form)
        self.addBook_frame.setGeometry(QtCore.QRect(100, 140, 681, 501))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addBook_frame.setFont(font)
        self.addBook_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addBook_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addBook_frame.setObjectName("addBook_frame")
        self.bookTitle_label = QtWidgets.QLabel(self.addBook_frame)
        self.bookTitle_label.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.bookTitle_label.setObjectName("bookTitle_label")
        self.bookTitle_lineEdit = QtWidgets.QLineEdit(self.addBook_frame)
        self.bookTitle_lineEdit.setGeometry(QtCore.QRect(130, 30, 341, 35))
        self.bookTitle_lineEdit.setObjectName("bookTitle_lineEdit")
        self.isbn_label = QtWidgets.QLabel(self.addBook_frame)
        self.isbn_label.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.isbn_label.setObjectName("isbn_label")
        self.isbn_lineEdit = QtWidgets.QLineEdit(self.addBook_frame)
        self.isbn_lineEdit.setGeometry(QtCore.QRect(130, 70, 231, 35))
        self.isbn_lineEdit.setObjectName("isbn_lineEdit")
        self.author_label = QtWidgets.QLabel(self.addBook_frame)
        self.author_label.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.author_label.setObjectName("author_label")
        self.author_comboBox = QtWidgets.QComboBox(self.addBook_frame)
        self.author_comboBox.setGeometry(QtCore.QRect(130, 110, 231, 35))
        self.author_comboBox.setObjectName("author_comboBox")
        self.category_label = QtWidgets.QLabel(self.addBook_frame)
        self.category_label.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.category_label.setObjectName("category_label")
        self.category_comboBox = QtWidgets.QComboBox(self.addBook_frame)
        self.category_comboBox.setGeometry(QtCore.QRect(130, 150, 221, 35))
        self.category_comboBox.setObjectName("category_comboBox")
        self.cover_label = QtWidgets.QLabel(self.addBook_frame)
        self.cover_label.setGeometry(QtCore.QRect(10, 190, 71, 31))
        self.cover_label.setObjectName("cover_label")
        self.uploadCover_button = QtWidgets.QPushButton(self.addBook_frame)
        self.uploadCover_button.setGeometry(QtCore.QRect(130, 190, 31, 35))
        self.uploadCover_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.uploadCover_button.setObjectName("uploadCover_button")
        self.coverPath_label = QtWidgets.QLabel(self.addBook_frame)
        self.coverPath_label.setGeometry(QtCore.QRect(170, 190, 381, 31))
        self.coverPath_label.setText("")
        self.coverPath_label.setObjectName("coverPath_label")
        self.preview_button = QtWidgets.QPushButton(self.addBook_frame)
        self.preview_button.setGeometry(QtCore.QRect(560, 190, 91, 31))
        self.preview_button.setObjectName("preview_button")
        self.description_label = QtWidgets.QLabel(self.addBook_frame)
        self.description_label.setGeometry(QtCore.QRect(10, 230, 121, 31))
        self.description_label.setObjectName("description_label")
        self.description_plainTextEdit = QtWidgets.QPlainTextEdit(self.addBook_frame)
        self.description_plainTextEdit.setGeometry(QtCore.QRect(130, 230, 391, 181))
        self.description_plainTextEdit.setObjectName("description_plainTextEdit")
        self.addBook_button = QtWidgets.QPushButton(self.addBook_frame)
        self.addBook_button.setGeometry(QtCore.QRect(130, 430, 191, 41))
        self.addBook_button.setObjectName("addBook_button")
        self.clearAll_button = QtWidgets.QPushButton(self.addBook_frame)
        self.clearAll_button.setGeometry(QtCore.QRect(330, 430, 191, 41))
        self.clearAll_button.setObjectName("clearAll_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addBook_label.setText(_translate("Form", "Add book"))
        self.bookTitle_label.setText(_translate("Form", "Title:"))
        self.isbn_label.setText(_translate("Form", "ISBN:"))
        self.author_label.setText(_translate("Form", "Author:"))
        self.category_label.setText(_translate("Form", "Category:"))
        self.cover_label.setText(_translate("Form", "Cover:"))
        self.uploadCover_button.setText(_translate("Form", "..."))
        self.preview_button.setText(_translate("Form", "Preview"))
        self.description_label.setText(_translate("Form", "Description:"))
        self.addBook_button.setText(_translate("Form", "Add book"))
        self.clearAll_button.setText(_translate("Form", "Clear all"))

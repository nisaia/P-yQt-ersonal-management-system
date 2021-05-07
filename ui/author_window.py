# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/author_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_author_window(object):
    def setupUi(self, author_window):
        author_window.setObjectName("author_window")
        author_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(author_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(author_window)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.wikipedia = QtWidgets.QLabel(self.tab)
        self.wikipedia.setAlignment(QtCore.Qt.AlignCenter)
        self.wikipedia.setOpenExternalLinks(True)
        self.wikipedia.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.wikipedia.setObjectName("wikipedia")
        self.gridLayout.addWidget(self.wikipedia, 2, 0, 1, 1)
        self.surname = QtWidgets.QLabel(self.tab)
        self.surname.setAlignment(QtCore.Qt.AlignCenter)
        self.surname.setObjectName("surname")
        self.gridLayout.addWidget(self.surname, 1, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.tab)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.editAuthor_label = QtWidgets.QLabel(self.tab_2)
        self.editAuthor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.editAuthor_label.setObjectName("editAuthor_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.editAuthor_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.name_label = QtWidgets.QLabel(self.tab_2)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.isbn_label = QtWidgets.QLabel(self.tab_2)
        self.isbn_label.setObjectName("isbn_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.isbn_label)
        self.surname_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.surname_lineEdit.setObjectName("surname_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.surname_lineEdit)
        self.editAuthor_button = QtWidgets.QPushButton(self.tab_2)
        self.editAuthor_button.setObjectName("editAuthor_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.editAuthor_button)
        self.deleteAuthor_button = QtWidgets.QPushButton(self.tab_2)
        self.deleteAuthor_button.setObjectName("deleteAuthor_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.deleteAuthor_button)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(author_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(author_window)

    def retranslateUi(self, author_window):
        _translate = QtCore.QCoreApplication.translate
        author_window.setWindowTitle(_translate("author_window", "Form"))
        self.wikipedia.setText(_translate("author_window", "Wikipedia"))
        self.surname.setText(_translate("author_window", "Surname"))
        self.name.setText(_translate("author_window", "Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("author_window", "Details"))
        self.editAuthor_label.setText(_translate("author_window", "Edit author"))
        self.name_label.setText(_translate("author_window", "Name:"))
        self.isbn_label.setText(_translate("author_window", "Surname:"))
        self.editAuthor_button.setText(_translate("author_window", "Edit author"))
        self.deleteAuthor_button.setText(_translate("author_window", "Delete author"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("author_window", "Edit/Delete"))

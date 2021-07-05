# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/allBooks_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allBooks_window(object):
    def setupUi(self, allBooks_window):
        allBooks_window.setObjectName("allBooks_window")
        allBooks_window.resize(890, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(allBooks_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allBooks_label = QtWidgets.QLabel(allBooks_window)
        self.allBooks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.allBooks_label.setObjectName("allBooks_label")
        self.verticalLayout.addWidget(self.allBooks_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.searchBook_lineEdit = QtWidgets.QLineEdit(allBooks_window)
        self.searchBook_lineEdit.setPlaceholderText('Search book by [Title - ISBN - Author - Genre - Status]')
        self.searchBook_lineEdit.setObjectName("searchBook_lineEdit")
        self.verticalLayout.addWidget(self.searchBook_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.allBooks_tableView = QtWidgets.QTableView(allBooks_window)
        self.allBooks_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allBooks_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.allBooks_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.allBooks_tableView.verticalHeader().setVisible(False)
        self.allBooks_tableView.setCursor(QtCore.Qt.PointingHandCursor)
        self.allBooks_tableView.setObjectName("allBooks_tableView")
        self.verticalLayout.addWidget(self.allBooks_tableView)

        self.retranslateUi(allBooks_window)
        QtCore.QMetaObject.connectSlotsByName(allBooks_window)

    def retranslateUi(self, allBooks_window):
        _translate = QtCore.QCoreApplication.translate
        allBooks_window.setWindowTitle(_translate("allBooks_window", "Form"))
        self.allBooks_label.setText(_translate("allBooks_window", "All books"))
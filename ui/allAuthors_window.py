# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/allAuthors_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allAuthors_window(object):
    def setupUi(self, allAuthors_window):
        allAuthors_window.setObjectName("allAuthors_window")
        allAuthors_window.resize(890, 730)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(allAuthors_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.allAuthors_label = QtWidgets.QLabel(allAuthors_window)
        self.allAuthors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.allAuthors_label.setObjectName("allAuthors_label")
        self.verticalLayout_2.addWidget(self.allAuthors_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.searchAuthor_lineEdit = QtWidgets.QLineEdit(allAuthors_window)
        self.searchAuthor_lineEdit.setPlaceholderText('Search author by [Name - Surname]')
        self.searchAuthor_lineEdit.setObjectName("searchAuthor_lineEdit")
        self.verticalLayout_2.addWidget(self.searchAuthor_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.allAuthors_tableView = QtWidgets.QTableView(allAuthors_window)
        self.allAuthors_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allAuthors_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.allAuthors_tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.allAuthors_tableView.verticalHeader().setVisible(False)
        self.allAuthors_tableView.setCursor(QtCore.Qt.PointingHandCursor)
        self.allAuthors_tableView.setObjectName("allAuthors_tableView")
        self.verticalLayout_2.addWidget(self.allAuthors_tableView)

        self.retranslateUi(allAuthors_window)
        QtCore.QMetaObject.connectSlotsByName(allAuthors_window)

    def retranslateUi(self, allAuthors_window):
        _translate = QtCore.QCoreApplication.translate
        allAuthors_window.setWindowTitle(_translate("allAuthors_window", "Form"))
        self.allAuthors_label.setText(_translate("allAuthors_window", "All authors"))

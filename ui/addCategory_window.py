# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/XML/addCategory_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addCategory_window(object):
    def setupUi(self, addCategory_window):
        addCategory_window.setObjectName("addCategory_window")
        addCategory_window.resize(890, 730)
        addCategory_window.setStyleSheet("QLabel#addCategory_label {\n"
"    background-color: green;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addCategory_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(addCategory_window)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.categoryName_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.categoryName_label.setFont(font)
        self.categoryName_label.setObjectName("categoryName_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.categoryName_label)
        self.categoryName_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.categoryName_lineEdit.setObjectName("categoryName_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.categoryName_lineEdit)
        self.addCategory_button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addCategory_button.setFont(font)
        self.addCategory_button.setObjectName("addCategory_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addCategory_button)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(addCategory_window)
        QtCore.QMetaObject.connectSlotsByName(addCategory_window)

    def retranslateUi(self, addCategory_window):
        _translate = QtCore.QCoreApplication.translate
        addCategory_window.setWindowTitle(_translate("addCategory_window", "Form"))
        self.categoryName_label.setText(_translate("addCategory_window", "Name:"))
        self.addCategory_button.setText(_translate("addCategory_window", "Add category"))
        self.label.setText(_translate("addCategory_window", "Add category"))
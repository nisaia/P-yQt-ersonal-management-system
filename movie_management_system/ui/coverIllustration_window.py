# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/coverIllustration_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_coverIllustration_window(object):
    def setupUi(self, coverIllustration_window):
        coverIllustration_window.setObjectName("coverIllustration_window")
        coverIllustration_window.resize(400, 500)
        self.horizontalLayout = QtWidgets.QHBoxLayout(coverIllustration_window)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.coverIllustration_label = QtWidgets.QLabel(coverIllustration_window)
        self.coverIllustration_label.setText("")
        self.coverIllustration_label.setObjectName("coverIllustration_label")
        self.horizontalLayout.addWidget(self.coverIllustration_label)

        self.retranslateUi(coverIllustration_window)
        QtCore.QMetaObject.connectSlotsByName(coverIllustration_window)

    def retranslateUi(self, coverIllustration_window):
        _translate = QtCore.QCoreApplication.translate
        coverIllustration_window.setWindowTitle(_translate("coverIllustration_window", "Dialog"))
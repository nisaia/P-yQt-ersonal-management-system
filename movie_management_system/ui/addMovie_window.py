# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_management_system/assets/XML/addMovie_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMovie_window(object):
    def setupUi(self, addMovie_window):
        addMovie_window.setObjectName("addMovie_window")
        addMovie_window.resize(890, 730)
        self.formLayout = QtWidgets.QFormLayout(addMovie_window)
        self.formLayout.setObjectName("formLayout")
        self.addMovie_label = QtWidgets.QLabel(addMovie_window)
        self.addMovie_label.setAlignment(QtCore.Qt.AlignCenter)
        self.addMovie_label.setObjectName("addMovie_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.addMovie_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.movieTitle_label = QtWidgets.QLabel(addMovie_window)
        self.movieTitle_label.setObjectName("movieTitle_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.movieTitle_label)
        self.movieTitle_lineEdit = QtWidgets.QLineEdit(addMovie_window)
        self.movieTitle_lineEdit.setObjectName("movieTitle_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.movieTitle_lineEdit)
        self.movieYear_label = QtWidgets.QLabel(addMovie_window)
        self.movieYear_label.setObjectName("movieYear_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.movieYear_label)
        self.movieYear_comboBox = QtWidgets.QComboBox(addMovie_window)
        self.movieYear_comboBox.setObjectName("movieYear_comboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.movieYear_comboBox)
        self.filmDirector_label = QtWidgets.QLabel(addMovie_window)
        self.filmDirector_label.setObjectName("filmDirector_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.filmDirector_label)
        self.filmDirector_comboBox = QtWidgets.QComboBox(addMovie_window)
        self.filmDirector_comboBox.setObjectName("filmDirector_comboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.filmDirector_comboBox)
        self.movieGenre_label = QtWidgets.QLabel(addMovie_window)
        self.movieGenre_label.setObjectName("movieGenre_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.movieGenre_label)
        self.movieGenre_comboBox = QtWidgets.QComboBox(addMovie_window)
        self.movieGenre_comboBox.setObjectName("movieGenre_comboBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.movieGenre_comboBox)
        self.movieCover_label = QtWidgets.QLabel(addMovie_window)
        self.movieCover_label.setObjectName("movieCover_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.movieCover_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uploadCover_button = QtWidgets.QPushButton(addMovie_window)
        self.uploadCover_button.setObjectName("uploadCover_button")
        self.horizontalLayout.addWidget(self.uploadCover_button)
        self.movieCoverPath_label = QtWidgets.QLabel(addMovie_window)
        self.movieCoverPath_label.setText("")
        self.movieCoverPath_label.setVisible(False)
        self.movieCoverPath_label.setObjectName("movieCoverPath_label")
        self.horizontalLayout.addWidget(self.movieCoverPath_label)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.moviePreview_button = QtWidgets.QPushButton(addMovie_window)
        self.moviePreview_button.setObjectName("moviePreview_button")
        self.moviePreview_button.setVisible(False)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.moviePreview_button)
        self.movieDescription_label = QtWidgets.QLabel(addMovie_window)
        self.movieDescription_label.setObjectName("movieDescription_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.movieDescription_label)
        self.movieDescription_plainTextEdit = QtWidgets.QPlainTextEdit(addMovie_window)
        self.movieDescription_plainTextEdit.setObjectName("movieDescription_plainTextEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.movieDescription_plainTextEdit)
        self.addMovie_button = QtWidgets.QPushButton(addMovie_window)
        self.addMovie_button.setObjectName("addMovie_button")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.addMovie_button)
        self.clearAll_button = QtWidgets.QPushButton(addMovie_window)
        self.clearAll_button.setObjectName("clearAll_button")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.clearAll_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.filmLength_label = QtWidgets.QLabel(addMovie_window)
        self.filmLength_label.setObjectName("filmLength_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.filmLength_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hour_label = QtWidgets.QLabel(addMovie_window)
        self.hour_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label.setObjectName("hour_label")
        self.horizontalLayout_2.addWidget(self.hour_label)
        self.hour_spinBox = QtWidgets.QSpinBox(addMovie_window)
        self.hour_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_spinBox.setMaximum(100)
        self.hour_spinBox.setObjectName("hour_spinBox")
        self.horizontalLayout_2.addWidget(self.hour_spinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.minutes_label = QtWidgets.QLabel(addMovie_window)
        self.minutes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.minutes_label.setObjectName("minutes_label")
        self.horizontalLayout_2.addWidget(self.minutes_label)
        self.minutes_spinBox = QtWidgets.QSpinBox(addMovie_window)
        self.minutes_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.minutes_spinBox.setMaximum(59)
        self.minutes_spinBox.setObjectName("minutes_spinBox")
        self.horizontalLayout_2.addWidget(self.minutes_spinBox)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.filmStatus_label = QtWidgets.QLabel(addMovie_window)
        self.filmStatus_label.setObjectName("filmStatus_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.filmStatus_label)
        self.filmStatus_comboBox = QtWidgets.QComboBox(addMovie_window)
        self.filmStatus_comboBox.setObjectName("filmStatus_comboBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.filmStatus_comboBox)

        self.retranslateUi(addMovie_window)
        QtCore.QMetaObject.connectSlotsByName(addMovie_window)

    def retranslateUi(self, addMovie_window):
        _translate = QtCore.QCoreApplication.translate
        addMovie_window.setWindowTitle(_translate("addMovie_window", "Form"))
        self.addMovie_label.setText(_translate("addMovie_window", "Add movie"))
        self.movieTitle_label.setText(_translate("addMovie_window", "Title:"))
        self.movieYear_label.setText(_translate("addMovie_window", "Year:"))
        self.filmDirector_label.setText(_translate("addMovie_window", "Film director:"))
        self.movieGenre_label.setText(_translate("addMovie_window", "Genre:"))
        self.movieCover_label.setText(_translate("addMovie_window", "Cover:"))
        self.uploadCover_button.setText(_translate("addMovie_window", "..."))
        self.moviePreview_button.setText(_translate("addMovie_window", "Preview"))
        self.movieDescription_label.setText(_translate("addMovie_window", "Description:"))
        self.addMovie_button.setText(_translate("addMovie_window", "Add movie"))
        self.clearAll_button.setText(_translate("addMovie_window", "Clear all"))
        self.filmLength_label.setText(_translate("addMovie_window", "Length:"))
        self.hour_label.setText(_translate("addMovie_window", "Hour"))
        self.minutes_label.setText(_translate("addMovie_window", "Minutes"))
        self.filmStatus_label.setText(_translate("addMovie_window", "Status:"))

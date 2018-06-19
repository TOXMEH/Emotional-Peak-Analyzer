# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score_viewer_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(179, 232)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(30, 50, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 7), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDate(QtCore.QDate(2018, 4, 7))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Form)
        self.dateEdit_2.setGeometry(QtCore.QRect(30, 110, 110, 22))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 5, 29), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setDate(QtCore.QDate(2018, 5, 29))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 121, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Начальная дата"))
        self.label_3.setText(_translate("Form", "Конечная дата"))
        self.pushButton.setText(_translate("Form", "Построить график"))

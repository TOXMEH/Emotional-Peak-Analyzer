# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotional_graph.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 275)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 101, 16))
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(30, 50, 62, 22))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(30, 110, 110, 22))
        self.dateEdit.setDate(QtCore.QDate(2018, 4, 7))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Form)
        self.dateEdit_2.setGeometry(QtCore.QRect(30, 170, 110, 22))
        self.dateEdit_2.setDate(QtCore.QDate(2018, 5, 29))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(240, 50, 95, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 70, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 90, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 101, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 120, 161, 16))
        self.label_5.setObjectName("label_5")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(240, 150, 22, 51))
        self.verticalSlider.setMaximum(1)
        self.verticalSlider.setProperty("value", 1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(270, 150, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 180, 101, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Epsilom"))
        self.label_2.setText(_translate("Form", "Начальная дата"))
        self.label_3.setText(_translate("Form", "Конечная дата"))
        self.radioButton.setText(_translate("Form", "EUR/USD"))
        self.radioButton_2.setText(_translate("Form", "GBP/USD"))
        self.radioButton_3.setText(_translate("Form", "USD/JPY"))
        self.label_4.setText(_translate("Form", "Валютная пара"))
        self.pushButton.setText(_translate("Form", "Построить график"))
        self.label_5.setText(_translate("Form", "Тим эмоционалной оценки"))
        self.label_6.setText(_translate("Form", "Положительная"))
        self.label_7.setText(_translate("Form", "Отрицательная"))

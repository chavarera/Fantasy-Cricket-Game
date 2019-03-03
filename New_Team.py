# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Team.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #LINE EDIT NAME FIRST INPUT BOX
        self.lename = QtWidgets.QLineEdit(Dialog)
        self.lename.setGeometry(QtCore.QRect(82, 109, 231, 41))
        self.lename.setObjectName("lename")

        #PUSH BUTTON FRO CREATING THE NEW TEAM
        self.btnCreate = QtWidgets.QPushButton(Dialog)
        self.btnCreate.setGeometry(QtCore.QRect(140, 180, 111, 41))
        self.btnCreate.setObjectName("btnCreate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Your Team Name"))
        self.btnCreate.setText(_translate("Dialog", "Create"))

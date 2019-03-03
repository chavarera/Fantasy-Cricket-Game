# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open_Team.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SqliteHandler import SqliteDataHandler as DataHandler
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 90, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #SIMPLE CREATE A COMBOBOX AND ADD A BLANK ITEM TO IT
        self.cbteamlist = QtWidgets.QComboBox(Dialog)
        self.cbteamlist.setGeometry(QtCore.QRect(120, 130, 151, 31))
        self.cbteamlist.setObjectName("cbteamlist")
        self.cbteamlist.addItem("Select")

        #button open to Select The Team
        self.open = QtWidgets.QPushButton(Dialog)
        self.open.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.open.setObjectName("open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select  Your Team"))
        self.open.setText(_translate("Dialog", "Open"))

        #Create a DAtabase Handler Object
        d1=DataHandler()

        #Fetch Team Name From Database
        teams = d1.FetachTeams()

        #Add return team list to Select List
        teamlist=[teams[i][0] for i in range(len(teams))]
        for name in set(teamlist):
            self.cbteamlist.addItem(name)

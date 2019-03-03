# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate_Score.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from SqliteHandler import  SqliteDataHandler as DataHandler
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbteam = QtWidgets.QComboBox(self.centralwidget)
        self.cbteam.setGeometry(QtCore.QRect(150, 70, 171, 31))
        self.cbteam.setObjectName("cbteam")
        self.cbmatch = QtWidgets.QComboBox(self.centralwidget)
        self.cbmatch.setGeometry(QtCore.QRect(370, 70, 171, 31))
        self.cbmatch.setObjectName("cbmatch")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 100, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(149, 130, 391, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.totalpoints = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalpoints.setFont(font)
        self.totalpoints.setObjectName("totalpoints")
        self.horizontalLayout.addWidget(self.totalpoints)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 190, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playerslist = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.playerslist.setObjectName("playerslist")
        self.verticalLayout.addWidget(self.playerslist)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 190, 211, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pointlist = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.pointlist.setObjectName("pointlist")
        self.verticalLayout_2.addWidget(self.pointlist)
        self.Evaluatescore = QtWidgets.QPushButton(self.centralwidget)
        self.Evaluatescore.setGeometry(QtCore.QRect(260, 410, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Evaluatescore.setFont(font)
        self.Evaluatescore.setObjectName("Evaluatescore")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Players"))
        self.label.setText(_translate("MainWindow", "Points"))
        self.totalpoints.setText(_translate("MainWindow", "0000"))
        self.Evaluatescore.setText(_translate("MainWindow", "Evaluate Score"))

        teams = []
        match = []
        d1=DataHandler()
        t = "select name,value from teams"
        teams = d1.FetchItems(t)
       #self.totalpnts = [int(t) for t in teams[0][1].split(",")]
        #self.ttlpnts = sum(self.totalpnts)
        allteams = [t[0] for t in teams]
        #self.cbteam.addItem("Select Team")
        #for i in range(len(allteams)):
        #   self.cbteam.addItem(allteams[i])
        self.totalpoints.setText("")
        self.cbmatch.addItem("Select Match")
        self.cbmatch.addItem("match")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


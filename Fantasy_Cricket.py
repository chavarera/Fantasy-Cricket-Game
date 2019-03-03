
#Import Basic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

#Import SQLITE HANDLER CLASS
from SqliteHandler import SqliteDataHandler as DataHandler

#Import Other Windows Here
from New_Team import Ui_Dialog as Form
from Open_Team import Ui_Dialog as OpenForm
from Evaluate_Score import Ui_MainWindow as EvaluateS
from Final_Score import  Ui_Dialog as FinalScore
#Some Basic Initilization Here
import sqlite3
mycricketapp = sqlite3.connect('Fantasyc.db')
curs = mycricketapp.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        #InITilize the NEW SCREEN WINDOW
        self.evalDialog = QtWidgets.QMainWindow()
        self.new_screen = Form()
        self.new_screen.setupUi(self.evalDialog)

        #OPEN ALREADY CREATED LIST
        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = OpenForm()
        self.open_screen.setupUi(self.openDialog)


        #Evaluate Window
        self.EvatulateDialog=QtWidgets.QMainWindow()
        self.evaluate_screen=EvaluateS()
        self.evaluate_screen.setupUi(self.EvatulateDialog)


        #Final Score Window
        self.ScoreDialog = QtWidgets.QMainWindow()
        self.score_screen = FinalScore()
        self.score_screen.setupUi(self.ScoreDialog)

    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setInformativeText("Are You Sure To Close It")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        msg.setWindowTitle("Waring")
        replay=msg.exec_()
        if(replay==QMessageBox.Yes):
            exit(0)
        else:
            pass

    def setupUi(self, MainWindow):
        self.batscount = 0
        self.weektcount = 0
        self.allroundscount = 0
        self.ballscount = 0
        self.totalscount = 0
        self.avipoints=1000
        self.usedpoints=0


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batsman = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batsman.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsman.setFont(font)
        self.batsman.setObjectName("batsman")
        self.horizontalLayout.addWidget(self.batsman)

        #Batsman Count
        self.batsmancount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batsmancount.setFont(font)
        self.batsmancount.setObjectName("batsmancount")
        self.horizontalLayout.addWidget(self.batsmancount)


        # Bowlers Count
        self.bowler = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowler.setFont(font)
        self.bowler.setObjectName("bowler")
        self.horizontalLayout.addWidget(self.bowler)

        self.bowlercount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bowlercount.setFont(font)
        self.bowlercount.setObjectName("bowlercount")
        self.horizontalLayout.addWidget(self.bowlercount)

        #Allrounder Count
        self.allrounder = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allrounder.setFont(font)
        self.allrounder.setObjectName("allrounder")
        self.horizontalLayout.addWidget(self.allrounder)

        self.allroundercount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.allroundercount.setFont(font)
        self.allroundercount.setObjectName("allroundercount")
        self.horizontalLayout.addWidget(self.allroundercount)

        #Weektkeeper Count
        self.weeketkeeper = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weeketkeeper.setFont(font)
        self.weeketkeeper.setObjectName("weeketkeeper")
        self.horizontalLayout.addWidget(self.weeketkeeper)

        self.wicketkeepercount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wicketkeepercount.setFont(font)
        self.wicketkeepercount.setObjectName("wicketkeepercount")
        self.horizontalLayout.addWidget(self.wicketkeepercount)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 111, 341, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PointsAvialable = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PointsAvialable.setFont(font)
        self.PointsAvialable.setObjectName("PointsAvialable")
        self.horizontalLayout_2.addWidget(self.PointsAvialable)
        self.pointsavialable = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pointsavialable.setFont(font)
        self.pointsavialable.setObjectName("pointsavialable")
        self.horizontalLayout_2.addWidget(self.pointsavialable)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(419, 110, 361, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pointused = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pointused.setFont(font)
        self.pointused.setObjectName("pointused")
        self.horizontalLayout_3.addWidget(self.pointused)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 341, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(419, 199, 361, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 340, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 150, 341, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BAT = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BAT.setFont(font)

        #BAT RADIOBUTTON
        self.BAT.setObjectName("BAT")
        self.horizontalLayout_4.addWidget(self.BAT)

        # BOW RADIOBUTTON
        self.BOW = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BOW.setFont(font)
        self.BOW.setObjectName("BOW")
        self.horizontalLayout_4.addWidget(self.BOW)

        #AR RADIOBUTTON
        self.AR = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AR.setFont(font)
        self.AR.setObjectName("AR")
        self.horizontalLayout_4.addWidget(self.AR)
        self.WK = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        #WK RADIOBUTTON
        self.WK.setFont(font)
        self.WK.setObjectName("WK")
        self.horizontalLayout_4.addWidget(self.WK)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(419, 149, 361, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.teamname = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.teamname.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_5.addWidget(self.teamname)
        MainWindow.setCentralWidget(self.centralwidget)


        #MENUBAR CODE
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #NEW TEAM You can use Ctrl+N TO Create new team
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionNEW_Team.setShortcut("Ctrl+N")
        self.actionNEW_Team.triggered.connect(self.new_file)

        #WHEN USER CLIK ON CREATE BUTTON GET TEXT FROM LINEEDIT AND CHANGE TEAM NAME
        self.new_screen.btnCreate.clicked.connect(self.ChangeTeamName)



        #OPEN TEAM
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionOPEN_Team.setShortcut("Ctrl+O")
        self.actionOPEN_Team.triggered.connect(self.Open_Team)

        #Now Clik on open button
        self.open_screen.open.clicked.connect(self.AfterOpenTeam)


        #SAVE TEAM
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.triggered.connect(self.Team_Save)
        self.actionSAVE_Team.setShortcut("Ctrl+S")



        #RADIO BUTTON CLICKED
        self.BAT.clicked.connect(self.Add_Team_Data)
        self.BOW.clicked.connect(self.Add_Team_Data)
        self.AR.clicked.connect(self.Add_Team_Data)
        self.WK.clicked.connect(self.Add_Team_Data)

        #Double Clicked items
        self.listWidget.itemDoubleClicked.connect(self.removefromraw)
        self.listWidget_2.itemDoubleClicked.connect(self.removefromfinal)




        #ADdd allselected Items

        self.items = []

        #EVALUATE TEAM
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEVALUATE_Team.triggered.connect(self.Evaluate_Score)
        self.actionEVALUATE_Team.setShortcut("Ctrl+E")

        #self.evaluate_screen.totalpoints.setText(str(self.evaluate_screen.ttlpnts))
        self.evaluate_screen.cbteam.currentTextChanged.connect(self.EvaluateScore)

        self.evaluate_screen.Evaluatescore.clicked.connect(self.Schow_score)


        self.score_screen.btnok.clicked.connect(self.CloseScore)




        #THIS CODE IS ADDED FOR APPLICATION EXIT PURPOSE
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionExit")
        self.actionEXIT.setShortcut("Ctrl+x")
        self.actionEXIT.triggered.connect(self.closeEvent)

        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addAction(self.actionEXIT)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def CloseScore(self):
        self.ScoreDialog.close()
    #---------------------FOR CREATING NEW TEAM-------------------------------------------#
    def new_file(self):
        self.evalDialog.show()
    def ChangeTeamName(self):
        #Get The Typed Name in line EDdit
        self.TeamName=self.new_screen.lename.text()

        #Set That Name To Team Name
        self.teamname.setText(self.TeamName)
        self.evalDialog.close()
    #----------------------------------END OF NEW TEAM----------------------------------#

    #Showing Players according to list
    def Add_Team_Data(self):
        checked=[self.BAT.isChecked(),self.BOW.isChecked(),self.AR.isChecked(),self.WK.isChecked()]
        sel=["BAT","BOW","AR","WK"]
        values=[sel[idx] for idx,c in enumerate(checked) if c==True]
        sql = "select player ||'-'|| ctg from players where ctg='{}'".format(values[0])

        #get Data
        d1=DataHandler()
        data=d1.FetchItems(sql)
        players=[d[0] for d in data]
        self.listWidget.clear()
        if(len(players)!=0):
            for i in range(len(players)):
                item = QtWidgets.QListWidgetItem(players[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(100)
                item.setFont(font)
                item.setBackground(QtGui.QColor('light gray'))
                self.listWidget.addItem(item)
    def GetPlayerpoints(self,name):
        sql="select value from stats where name='{}'".format(name)
        d1=DataHandler()
        data=d1.FetchItems(sql)
        return data[0][0]

    def PointsSet(self,selectedit):
        points = self.GetPlayerpoints(selectedit)
        self.avipoints -= points
        self.pointsavialable.setText(str(self.avipoints))
        pointsused = 1000 - self.avipoints
        self.pointused.setText(str(pointsused))

    def removefromraw(self,item):
        self.check2=[]
        for i in range(self.listWidget_2.count()):
            items=self.listWidget_2.item(i).text()
            self.check2.append(items)
        selectedit=str(self.listWidget.currentItem().text()).split("-")[0]
        if(self.listWidget.currentItem().text() not in self.check2):

            if self.avipoints >= 0:
                # IF BAT is Clicked
                if self.BAT.isChecked() == True:
                    if self.batscount >= 0 and self.batscount < 5:
                        self.PointsSet(selectedit)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.listWidget_2.addItem(item)
                        self.batscount += 1
                        self.totalscount = self.listWidget.count()
                        self.batsmancount.setText(str(self.batscount))
                    else:
                        msg = "Only 5 batsman are allowed"
                        self.ShowError(msg)

                # FOR WEEKETKEEPER
                elif self.WK.isChecked() == True:
                    if self.weektcount >= 0 and self.weektcount < 1:
                        self.PointsSet(selectedit)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.listWidget_2.addItem(item)
                        self.weektcount += 1
                        self.totalscount = self.listWidget.count()
                        self.wicketkeepercount.setText(str(self.weektcount))
                    else:
                        msg = "Only 1 keeper are allowed"
                        self.ShowError(msg)
                # FOR ALLROUNDER
                elif self.AR.isChecked() == True:
                    if self.allroundscount >= 0 and self.allroundscount < 2:
                        self.PointsSet(selectedit)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.listWidget_2.addItem(item)
                        self.allroundscount += 1
                        self.allroundercount.setText(str(self.allroundscount))
                    else:
                        msg = "Only 2 Allrounder Count"
                        self.ShowError(msg)
                ##FOR BALLER
                else:
                    if self.ballscount >= 0 and self.ballscount < 3:
                        self.PointsSet(selectedit)
                        self.listWidget.takeItem(self.listWidget.row(item))
                        self.listWidget_2.addItem(item)
                        self.ballscount += 1
                        self.bowlercount.setText(str(self.ballscount))
                    else:
                        msg = "Only 3 bowlers are allowed"
                        self.ShowError(msg)
            else:
                message="Remaing Points are Less to select this player"
                self.ShowError(message)

        else:
            self.ShowError("already Selected")


    def SetPoints(self):
        print("gi")


    def removefromfinal(self,item):
        self.check = []
        for i in range(self.listWidget.count()):
            items = self.listWidget.item(i).text()
            self.check.append(items)
        checked = [self.BAT.isChecked(), self.BOW.isChecked(), self.AR.isChecked(), self.WK.isChecked()]
        sel = ["BAT", "BOW", "AR", "WK"]
        values = [sel[idx] for idx, c in enumerate(checked) if c == True]
        citem=values[0]
        selectitems=self.listWidget_2.currentItem().text().split("-")[1]
        selectid=self.listWidget_2.currentItem().text().split("-")[0]
        cs=self.listWidget_2.currentItem().text()#current selected Item

        points = self.GetPlayerpoints(selectid)
        self.avipoints += points
        self.pointsavialable.setText(str(self.avipoints))
        pointsused = 1000 - self.avipoints
        self.pointused.setText(str(pointsused))


        if selectitems=="BAT":
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            if(citem=="BAT") and cs not in self.check :
                self.listWidget.addItem(item)
            self.batscount -= 1
            self.batsmancount.setText(str(self.batscount))




            # FOR WEEKETKEEPER
        elif  selectitems=="WK":
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            if (citem == "WK") and  cs not in self.check:
                self.listWidget.addItem(item)
            self.weektcount -= 1
            self.wicketkeepercount.setText(str(self.weektcount))

        # FOR ALLROUNDER
        elif  selectitems=="AR":
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            if (citem == "AR") and cs not in self.check:
                self.listWidget.addItem(item)
            self.allroundscount -= 1
            self.allroundercount.setText(str(self.allroundscount))

        ##FOR BALLER
        else:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            if (citem == "BOW") and cs not in self.check:
                self.listWidget.addItem(item)
            self.ballscount -= 1
            self.bowlercount.setText(str(self.ballscount))



    #----------------------------OPEN TEAM------------------------------------------#
    def ShowSuccess(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Success")
        msg.setInformativeText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def ShowError(self,e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(e)
        msg.setWindowTitle("Error")
        msg.exec_()

    def Open_Team(self):
        self.openDialog.show()


    def AfterOpenTeam(self):
        self.selected =self.open_screen.cbteamlist.currentText()
        if str(self.selected)!="Select":
            d1=DataHandler()
            sqlq = "select * from teams where name='{}'".format(self.selected)
            data = d1.FetchItems(sqlq)
            TeamName=data[0][0]
            players=data[0][1].split(",")
            self.listWidget_2.clear()
            self.teamname.setText(TeamName)
            for i in range(len(players)) :
                item = QtWidgets.QListWidgetItem(players[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(100)
                item.setFont(font)
                item.setBackground(QtGui.QColor('light gray'))
                self.listWidget_2.addItem(item)
            self.openDialog.close()
        else:
            e="Please Select At least one Team"
            self.ShowError(e)

    # ----------------------------END OPEN TEAM------------------------------------------#

    def Team_Save(self):
        self.items.clear()
        for index in range(self.listWidget_2.count()):
            self.items.append(self.listWidget_2.item(index).text().split("-")[0])
        d1=DataHandler()
        scoresdata = []
        for player in self.items:
            squery="select value from stats where name='{}';".format(player)
            data=str(d1.FetchItems(squery)[0][0])
            scoresdata.append(data)
        #List = tuple(zip(self.items, score))
        name=self.teamname.text()
        players=",".join(self.items)
        scores=",".join(scoresdata)
        if(len(self.items)==11):
            checkteams="select name from teams where name='{}'".format(name)
            checkvalue=d1.FetchItems(checkteams)
            if (len(checkvalue)>0):
                e = "This Team Name is Already Exists"
                self.ShowError(e)
            elif(name=="#####"):
                e = "Blank Team Name Not Allowed"
                self.ShowError(e)

            else:
                sqladdteam = "Insert into teams (name,players,value) values(?,?,?)"
                inserteddata = d1.InsertItems(sqladdteam, (name, players, scores))
                if(inserteddata=="1"):
                    message="Successfully Saved"
                    self.ShowSuccess(message)
                else:
                    e = "Something Went Wrong Try Again"
                    self.ShowError(e)



        else:
            e = "Please Select At least 11 Players"
            self.ShowError(e)

    def Evaluate_Score(self):
        d1 = DataHandler()
        t = "select name,value from teams"
        teams = d1.FetchItems(t)
        allteams = [t[0] for t in teams]
        self.evaluate_screen.cbteam.addItem("Select Team")
        for i in range(len(allteams)):
            self.evaluate_screen.cbteam.addItem(allteams[i])
        self.EvatulateDialog.show()
    def EvaluateScore(self):
        self.evaluate_screen.cbmatch.currentTextChanged.connect(self.FinalScore)
    def PlayerScoreCalulate(self,coloumns,d1,name):
        sql="select * from match where player='{}'".format(name)
        data=d1.FetchItems(sql)
        player_score=[]
        scored=data[0][1]
        try:
            strikerate=(scored/data[0][2])*100
        except:
            strikerate=0
        #Batsman Scored
        #1point for each 2 run
        try:
            player_score.append(scored/2)
        except:
            pass

        #if scored>50 then 5 points
        if(scored>=50):
            player_score.append(int(scored/50)*5)


        #if Strikerate is greator than 100 then extra 4 points
        if (scored >= 100):
            player_score.append(int(scored/100)*10)

        #if strikerate is 80-100 the extra 4 points
        if 80<=strikerate<=100:
            player_score.append(2)

        #per 4 1 point
        if data[0][3]>0:
            player_score.append(1*data[0][3])


        #per 6 2 points
        if data[0][4]>0:
            player_score.append(2*data[0][4])


        #FOR Bowling
        #per wicket 10 points
        wkt=data[0][8]
        if wkt>0:
            player_score.append(10 * wkt)

        #if wickets are greator than 3 the 5 points
        if 3<=wkt<=5:
            player_score.append(5)

        #if wicket is greator or equql to 5 then extra 10 points
        if wkt>5:
            player_score.append(10)



        #ECONOMY RRATE
        overs=data[0][5]/6
        givenruns=data[0][7]
        try:
            economyrate = givenruns / overs
        except:
            economyrate=0

        #if economy rate between 3.5 to 4.5 then 4 points
        if 3.5<=economyrate<=4.5:
            player_score.append(4)


        #economy rate between 2 to 3.5 then 7 points
        if 2<=economyrate<=3.5:
            player_score.append(7)

        #economy rate less than 2 them 10 points
        if economyrate<2:
            player_score.append(10)

        #10  points  each for catch / stumping / run out
        catch=data[0][9]*10
        stump=data[0][10]*10
        runout=data[0][11]*10

        player_score.extend([catch,stump,runout])

        #print(sum(player_score),player_score)

        #All Points Generated using rules
        return  sum(player_score)
    def FinalScore(self):
        scores=[]
        d1 = DataHandler()
        #Get All Required Coloumns
        sql = "select * from match;"
        coloumnslist = d1.Fetchcoloumns(sql)
        team=self.evaluate_screen.cbteam.currentText()
        psql ="select players from teams where name='{}'".format(team)
        pls=list(d1.FetchItems(psql)[0])
        playerlist=pls[0].split(",")
        self.evaluate_screen.pointlist.clear()
        self.evaluate_screen.playerslist.clear()
        for index in range(len(playerlist)):
            playerscore=self.PlayerScoreCalulate(coloumnslist,d1,playerlist[index])
            item = QtWidgets.QListWidgetItem(playerlist[index])
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setBackground(QtGui.QColor('#ffff99'))
            self.evaluate_screen.playerslist.addItem(item)
            self.evaluate_screen.pointlist.addItem(str(playerscore))

    def Schow_score(self):

        pointcount=self.evaluate_screen.pointlist.count()
        self.scorepoints=[((self.evaluate_screen.pointlist.item(i).text())) for i in range(pointcount)]
        self.adds=0
        for sp in self.scorepoints:
            self.adds+=float(sp)

        if(self.evaluate_screen.cbteam.currentText()!="Select Team" and self.evaluate_screen.cbteam.currentText()!="Select Match"):
            self.ScoreDialog.show()
            d1 = DataHandler()
            squry = "Update teams set value=? where name=?"
            data = d1.InsertItems(squry, (self.adds, self.evaluate_screen.cbteam.currentText()))
            self.score_screen.label_2.setText('{}'.format(self.adds))
        else:
            message="Please Select team And Match"
            self.ShowError(message)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.batsman.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.batsmancount.setText(_translate("MainWindow", "##"))
        self.bowler.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bowlercount.setText(_translate("MainWindow", "##"))
        self.allrounder.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.allroundercount.setText(_translate("MainWindow", "##"))
        self.weeketkeeper.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.wicketkeepercount.setText(_translate("MainWindow", "##"))
        self.PointsAvialable.setText(_translate("MainWindow", "Points Avialable"))
        self.pointsavialable.setText(_translate("MainWindow", "####"))
        self.label.setText(_translate("MainWindow", "Points Used"))
        self.pointused.setText(_translate("MainWindow", "####"))
        self.label_13.setText(_translate("MainWindow", ">"))
        self.BAT.setText(_translate("MainWindow", "BAT"))
        self.BOW.setText(_translate("MainWindow", "BOW"))
        self.AR.setText(_translate("MainWindow", "AR"))
        self.WK.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.teamname.setText(_translate("MainWindow", "#####"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))
        self.pointsavialable.setText(str(self.avipoints))
        self.pointused.setText(str(self.usedpoints))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


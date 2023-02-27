import cursorManip as cursor
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("acp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 161, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setStyleSheet("border-radius: 11.33px;font: 75 22.3pt \"Calibri\";background-color: rgb(172, 212, 255);border: 1px dashed black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setStyleSheet("color: black; font: 87 11pt \"Arial\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setStyleSheet("border-radius: 11.33px; font: 75 22.3pt \"Calibri\"; background-color: rgb(172, 212, 255); border: 1px dashed black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet("color: black; font: 87 11pt \"Arial\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(283, 145, 211, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setStyleSheet("border-radius: 13px;font: 75 22.3pt \"Calibri\";")
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setStyleSheet("border-radius: 13px;font: 75 22.3pt \"Calibri\";")
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(313, 85, 31, 61))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 75 33pt \"Calibri\"; font-weight: 700;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 90, 31, 51))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font: 75 33pt \"Calibri\"; font-weight: 700;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 340, 121, 54))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 75 18.33pt \"Calibri\"; font-weight: 700;")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(389, 350, 101, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_3.setStyleSheet("border-radius: 0px;font: 75 22.3pt \"Calibri\";")
        self.spinBox_3.setMaximum(9999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_2.addWidget(self.spinBox_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 181, 51))
        self.pushButton.setStyleSheet("border-radius: 11.33px;font: 75 22.3pt \"Calibri\";background-color: rgb(140, 255, 114);border: 3px solid black; font-weight: 700; font-style: italic;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 30, 181, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setStyleSheet("border-radius: 11.33px;font: 75 22.3pt \"Calibri\";background-color: rgb(172, 212, 255);border: 2.33px solid black; font-weight: 500;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("font: 75 23.33pt \"Calibri\"; font-weight:600;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(238, 280, 141, 39))
        self.pushButton_5.setStyleSheet("border-radius: 11.33px; font: 75 12.3pt \"Calibri\"; background-color: rgb(172, 212, 255); border: 0.5px solid black; font-weight: 700;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(389, 400, 101, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox_4.setStyleSheet("border-radius: 0px;font: 75 22.3pt \"Calibri\";")
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 400, 121, 54))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("font: 75 18.33pt \"Calibri\"; font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(15, 385, 181, 51))
        self.pushButton_6.setStyleSheet("border-radius: 11.33px;font: 75 22.3pt \"Calibri\";background-color: rgb(140, 255, 114);border: 3px solid black; font-weight: 700; font-style: italic;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 282, 141, 39))
        self.pushButton_7.setStyleSheet("border-radius: 11.33px; font: 75 12.3pt \"Calibri\"; background-color: rgb(172, 212, 255); border: 0.5px solid black; font-weight: 700;")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReport_Bug = QtWidgets.QAction(MainWindow)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        self.actionRepositary = QtWidgets.QAction(MainWindow)
        self.actionRepositary.setObjectName("actionRepositary")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionRepositary)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        # ~~~~~~~ Modules
        #self.spinBox_3.setValue(9)
        #Icon

        #Icon
        
        self.pushButton_2.clicked.connect(lambda: cursor.setPos(self.label_5, self.spinBox_2, self.spinBox) ) #Set clicking position
        #!!!- change of presets
        #self.pushButton_3.clicked.connect(lambda: cursor.changePreset(self.checkBox_2, self.checkBox, self.spinBox_2, self.spinBox) )
        
        def labelChg(coordinate_tracker, x, y):
                coordinate_tracker.setText("("+str(x) + ", " + str(y)+ ")")

        def presetSetter(x, file, altBox, box, presetOn, coordinate_tracker):
                with open(file, 'r') as preset:
                        v = preset.read()
                        if altBox: ##
                                box.setChecked(False)
                        
                        if not presetOn: ##
                                return -1
                        coordinate_tracker.setText("("+v.split()[0]+", "+ v.split()[1] + ")")

                        x.spinBox_2.setValue(int(v.split()[0]))#Sets x Coord
                        x.spinBox.setValue(int(v.split()[1])) # Sets y coord

        self.pushButton_3.clicked.connect(lambda: presetSetter(self, "preset1.txt", self.checkBox_2.isChecked(), self.checkBox_2, self.checkBox.isChecked(), self.label_5)) #Fills in preset 1
        self.pushButton_4.clicked.connect(lambda: presetSetter(self, "preset2.txt", self.checkBox.isChecked(), self.checkBox, self.checkBox_2.isChecked(), self.label_5)) #Fills in preset 2
        
        
        #self.pushButton_5.clicked.connect(lambda: cursor.changePreset(self.checkBox, self.checkBox_2, self.spinBox_2.value(), self.spinBox.value()) ) # double bt so
        self.pushButton_7.clicked.connect(lambda: cursor.changePreset(self.checkBox, self.checkBox_2, self.spinBox_2.value(), self.spinBox.value()) )# same
        #self.pushButton_4.clicked.connect(lambda: presetSetter(self, "preset2.txt")) #Fills in preset 2
        
        
        self.pushButton_2.clicked.connect(lambda: cursor.moveFunc(self.spinBox_2.value(), self.spinBox.value(), .0033))
        #Clicker start function
        self.pushButton.clicked.connect(lambda: cursor.clickFunc(self.spinBox_2.value(), self.spinBox.value(), 0.013, self.spinBox_3.value(), self.doubleSpinBox_4.value()) )
        self.pushButton_6.clicked.connect(lambda: cursor.clickFunc(self.spinBox_2.value(), self.spinBox.value(), 0.013, self.spinBox_3.value(), self.doubleSpinBox_4.value()) )
        self.spinBox_2.valueChanged.connect(lambda: labelChg(self.label_5, self.spinBox_2.value(), self.spinBox.value()))
        self.spinBox.valueChanged.connect(lambda: labelChg(self.label_5, self.spinBox_2.value(), self.spinBox.value()))
        
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        #self.pushButton_3.clicked.connect(lambda: cursor.preset1(self.checkBox.isChecked()))
        
        # ~~~~~~~~~~~~~~~~~~~ Modules.E

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuickClick 1.0"))
        self.pushButton_3.setText(_translate("MainWindow", "Set Preset 1"))
        self.checkBox.setText(_translate("MainWindow", "Preset 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Set Preset 2"))
        self.checkBox_2.setText(_translate("MainWindow", "Preset 2"))
        self.spinBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:400; font-style:italic;\">Sets the x value manually</span></p></body></html>"))
        self.spinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic;\">Sets the x value manually</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Clicks"))
        self.pushButton.setText(_translate("MainWindow", "Start Clicker"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Position"))
        self.label_5.setText(_translate("MainWindow", "(0 , 0)"))
        self.pushButton_5.setText(_translate("MainWindow", "Change Preset"))
        self.label_4.setText(_translate("MainWindow", "Delay (Secs)"))
        self.pushButton_6.setText(_translate("MainWindow", "Start Clicker"))
        self.pushButton_7.setText(_translate("MainWindow", "Change Preset"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionReport_Bug.setText(_translate("MainWindow", "Report Bug"))
        self.actionRepositary.setText(_translate("MainWindow", "Github Repo"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
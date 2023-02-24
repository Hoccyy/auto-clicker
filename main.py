import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, \
    QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMessageBox, QMenuBar, QMenu, \
    QMainWindow

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication (sys.argv)

window = QWidget()
grid = QGridLayout ()
window.setLayout (grid)

widgets = {
    "Buttons" : [],
    "Labels" : [],
}

#Main window area
class mainWindow:
    # Uses parameters to set window specs
    def __init__ (self, width, height, title, style, icon):
        self.width = window.setFixedWidth (width)
        self.height = window.setFixedHeight (height)
        self.title = window.setWindowTitle (title)
        self.style = window.setStyleSheet (style)
        self.icon = window.setWindowIcon (icon)

class secondaryWindow (QMainWindow):
    # Uses parameters to set window specs
    def __init__ (self, width, height, title, style, icon):
        self.width = window.setMinimumWidth (width)
        self.height = window.setMinimumHeight (height)
        self.title = window.setWindowTitle (title)
        self.style = window.setStyleSheet (style)
        self.icon = window.setWindowIcon (icon)

        QLabel('DOg')
    
    def createMenu(self):
        menuBar - self.menuBar()
        #Add menu items
        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        helpMenu = menuBar.addMenu('Help')
        #Sub-items
        helpMenu.addAction(self, sendEmailAction)
        #Horiz Line
        helpMenu.addSeparator()




def frame0 ():
    # Creates the frame with the main window class
    #                  (Wid.) (hei.)    Title             Styles              Icon
    frameStyles = "background-color:red;"
    frame = mainWindow ((600), (600), "Auto Clicker", frameStyles, QtGui.QIcon ("ac.ico"))

def frame1 ():
    frame = secondaryWindow(600, 600, "Auto Clicker", "color: red;", QtGui.QIcon("ac.ico"))


frame1()
# Displays the window
window.show()

sys.exit (app.exec())
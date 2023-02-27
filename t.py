from PyQt5 import QtWidgets, QtGui, QtCore
from mywindow_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F8:
            print("F8 key pressed")

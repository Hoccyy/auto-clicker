from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("My PyQt App")
        MainWindow.setGeometry(100, 100, 400, 300)

        # Set the window flags to keep the window on top
        MainWindow.setWindowFlags(MainWindow.windowFlags() | Qt.WindowStaysOnTopHint)

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
import pyautogui as pagui
import time as t

def getPos():
    x,y = pyautogui.position()
    return x,y

def moveFunc(x, y, tt):
    #             Coords. and time
    #                 x, y, time(2)
    pagui.moveTo(x, y,  tt)

#pagui.moveTo(10_000, 10_000,  2)
#Function to click
def click():
    try:
        pagui.click()
        print (1)
    except:
        print (0)

def manChg0(self):
    #print(self.spinBox_2.value()) test if value is working
    if self.spinBox_2.value() > 9999:
            sys.exit(app.exec_())
            return 0
    xVal = self.spinBox_2.value()
    print(xVal)
    return 1

def fetchPreset1():
    with open("preset1.txt", 'r') as preset1:
        v = preset1.read()
        #print (int(v.split()[0])) ; print (int(v.split()[1]))
        return (v.split())

def  clickFunc(x, y, tt, rep):
    if rep < 1:
        return -1
    moveFunc(x, y, tt)
    for i in range(rep):
        pagui.click();print("i :3")

def setPos(coordinate_tracker, x, y):
    coordinate_tracker.setText("("+str(pagui.position()[0]) +", "+ str(pagui.position()[1]) + ")")
    x.setValue(pagui.position()[0])
    y.setValue(pagui.position()[1])

def changePreset(preset1, preset2, xVal, yVal):
    if preset1.isChecked() and preset2.isChecked():
        preset1.setChecked(False) ; preset2.setChecked(False)
        return -1

    if preset1.isChecked() or preset2.isChecked():
        if preset2.isChecked() and not preset1.isChecked():
            with open("preset1.txt", 'w') as preset1:
                preset1.write(str(xVal) + " " + str(yVal)) ; return 1
        with open("preset2.txt", 'w') as preset2:
            preset2.write(str(xVal) + " " + str(yVal))
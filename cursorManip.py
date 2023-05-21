import time       as tim
import webbrowser as web
import pyautogui  as pagui
import sys, subprocess, os, platform

#.   pagui.FAILSAFE = False
#Careful with ^^^ due to mouse spam failure issue, try to instead derive screen resolution per device
def getPos ():
    x, y = pagui.position()
    return x, y

#          x & y Coords, and time
def moveFunc (x, y, tt):
    #                 x, y, time(2)
    pagui.moveTo(x, y,  tt)

# Click function
def click ():
    try:
        pagui.click()
    except:
        return 1
# Coordinate preset fetcher
def fetchPreset1 ():
    with open("preset1.txt", 'r') as preset1:
        preset1FileData = preset1.read()
        return (preset1FileData.split())

def clickFunc (x, y, tt, repitions, delaySecs):
    if repitions < 1:
        return -1
    moveFunc (x, y, tt)
    
    if delaySecs != 0:
        for i in range (repitions):
            pagui.click()
            tim.sleep(delaySecs)
        return 1

    for i in range (repitions):
        pagui.click()#;print("Click")

def setPos (coordinate_tracker, x, y):
    try:
        coordinate_tracker.setText ("("+str(pagui.position()[0]) +", "+ str(pagui.position()[1]) + ")")
        x.setValue (pagui.position()[0])
        y.setValue (pagui.position()[1])
    except pyautogui.FailSafeException:
        print ("Failed")

def changePreset (preset1, preset2, xVal, yVal):
    if preset1.isChecked() and preset2.isChecked():
        preset1.setChecked (False)
        preset2.setChecked (False)
        return -1

    if (preset1.isChecked() or preset2.isChecked()):
        if preset1.isChecked() and not preset2.isChecked():
            with open("preset1.txt", 'w') as preset1_:
                preset1_.write(str(xVal) + " " + str(yVal))

            preset1.setChecked(False)
            return 1
        with open ("preset2.txt", 'w') as preset2_:
            preset2_.write(str(xVal) + " " + str(yVal)) ; 
        
        preset2.setChecked(False); return 1

def openManual ():
    filepath = 'Manual.txt'
    if platform.system() == 'Darwin':
        subprocess.call(('open', filepath))
        return 1
        
    if platform.system() == 'Windows':
        os.startfile(filepath)
        return 1
    else:
        subprocess.call(('xdg-open', filepath))
        return 1

#Menu methods for functionality
def openRepo ():
    repoLink = 'https://github.com/Hoccyy/auto-clicker'
    web.open(repoLink)
def reportBug ():
    bugReport = 'https://github.com/Hoccyy/auto-clicker/issues'
    web.open(bugReport)
def closeApp (ap):
    sys.exit(ap.exec_())

import pyautogui as pagui

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

def setPos():
    pagui.position()
import pyautogui as pagui


def getPos():
    x,y = pyautogui.position()
    return x,y

def moveFunc(x, y):
    #                 x, y, time
    pagui.moveTo(x, y,  2)

#Function to click
def click():
    try:
        pagui.click()
        print (1)
    except:
        print (0)
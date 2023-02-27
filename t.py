fileName = 'AutoClicker.py'


with open(fileName, 'r') as file:
    x = file.read()
    print((x.count("\n")+1))
import serial
import threading as t
import time
import random
import re
import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
#from tkinter import *
#ser = serial.Serial('/dev/ttyUSB0')
w = 0

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def gui():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

class myThread (t.Thread):
   def __init__(self, threadID, name, func):
      t.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.func = func

   def run(self):
      print("Starting " + self.name)
      globals()[self.func]()
      print("Exiting " + self.name)

def logicLoop(initWeight):
    global wlabel
    while(not w < 3 and initWeight > 0):
        wlabel.set(initWeight)

def newProduct():
    initialWeight = w
    print("New product initial weight = " + str(initialWeight))
    logicLoop(initialWeight)

def weightloop():
	while(1):
		global w
        #cweight = re.sub("[^\d+$.g]+", '', str(ser.readline()))
        #fweight = float(re.sub("[g]", '', cweight))
        #w = fweight
		w = random.randint(0,100)
		time.sleep(1)
		#print(fweight)
		print(w)

weightthread = myThread(1, "Weightthread" , "weightloop")
guithread = myThread(2 , "Gui" , "gui")

weightthread.start()
guithread.start()

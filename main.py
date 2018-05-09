import serial
import threading as t
import time
import re
import sys
from PyQt5 import QtGui
#from tkinter import *
ser = serial.Serial('/dev/ttyUSB0')
w = 0

def gui():
  app = QtGui.QApplication(sys.argv)
  win = QtGui.QWidget()
  b = QtGui.QLabel(win)
  b.setText("Hello World!")
  win.setGeometry(100,100,200,50)
  b.move(50,20)
  win.show()
  sys.exit(app.exec_())
  """
    master = Tk()
    wlabel = StringVar()
    global wlabel
    Label(master, textvariable=wlabel).pack()
    b = Button(master, text="Nyt Produkt", command=newProduct)
    b.pack()
    mainloop()"""

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
        cweight = re.sub("[^\d+$.g]+", '', str(ser.readline()))
        fweight = float(re.sub("[g]", '', cweight))
        w = fweight
        print(fweight)


weightthread = myThread(1, "Weightthread" , "weightloop")
guithread = myThread(2 , "Gui" , "gui")

weightthread.start()
guithread.start()

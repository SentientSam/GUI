#This file is for Classes tutorial use. Classes in tkinter work the same way they do with regular Python coding or C++
from tkinter import *
class ButtonClass: 
  def __init__(self,master): #__init__ is a function that will automatically initialize without having to be called
    frame = Frame(master) #the master is simply the master window (or "window")
    frame.pack()
    self.displayButton = Button(frame,text="Display Message",bg="red",command=self.displayMessage)
    self.displayButton.pack(side=LEFT)
    self.exitButton = Button(frame,text=" x ",bg="white",command=frame.quit) #frame.quit is a tkinter funtionality that breaks the main loop (exits)
    self.exitButton.pack(side=LEFT)
  def displayMessage(self):
    print("Classes aren't awful!")
window = Tk()
button = ButtonClass(window) #Once the object is created, it will automatically run everything within the class (due to __init__)
window.mainloop() #the loop will be ended when exiting the program, or by pressing the exit button
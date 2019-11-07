# Graphical User Interface Testing Project
# Tkinter
from tkinter import *

window = Tk() #Creating a window
#firstLabel = Label(window, text="GUI Test") #Creating a text label (text on the screen)
#firstLabel.pack() #pack it in there, wherever it will fit (pretty lazy, will improve later)
#Frame is like a text box within word. It is an invisible parameter
topFrame = Frame(window)
topFrame.pack()
btmFrame = Frame(window)
btmFrame.pack(side=BOTTOM)
button1 = Button(topFrame,text="Uno",fg="red")
button4 = Button(topFrame,text="Dos",fg="orange")
button2 = Button(btmFrame,text="Tres",fg="green")
button3 = Button(btmFrame,text="Quattro",fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)
window.mainloop() #loops this window (so that the window stays open until exited)

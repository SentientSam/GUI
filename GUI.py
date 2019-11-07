<<<<<<< HEAD
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
#Widgets go in 2 steps. Initializing, and then placing
button1.pack(side=LEFT) #packing with parameters will move these buttons. That way, rather than being on top of each other, these buttons will be beside one another
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
window.mainloop() #loops this window (so that the window stays open until exited)
=======
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
#Widgets go in 2 steps. Initializing, and then placing
button1.pack(side=LEFT) #packing with parameters will move these buttons. That way, rather than being on top of each other, these buttons will be beside one another
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
window.mainloop() #loops this window (so that the window stays open until exited)
>>>>>>> 345b3f2e7875f835653cb665afcd81dd92486cdf

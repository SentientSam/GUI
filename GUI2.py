<<<<<<< HEAD
from tkinter import*
window = Tk()

#Setting up frames is not necessary, it does however help to get used to them
unoFrame = Frame(window)
unoFrame.pack(fill=X) #If you want widgets to fill X, the frame will need to also
dosFrame = Frame(window)
dosFrame.pack(side=BOTTOM, fill=X)

Uno = Label(unoFrame, text="Uno", bg="blue", fg="yellow") #Background color is bg, Foreground color if fg
Uno.pack(side=TOP)
Dos = Label(unoFrame, text="Dos", bg="black", fg="yellow")
Dos.pack(fill=X) #The point of this file: If you fill to X or Y, no matter how you resize the window the label will fill the space.
Tres = Label(unoFrame, text="Tres", bg="red", fg="yellow")
Tres.pack(side=LEFT, fill=Y)

#Just to show again with a button
button1 = Button(dosFrame,text="Button",fg="orange",bg="blue")
button1.pack(fill=X)
=======
from tkinter import*
window = Tk()

#Setting up frames is not necessary, it does however help to get used to them
unoFrame = Frame(window)
unoFrame.pack(fill=X) #If you want widgets to fill X, the frame will need to also
dosFrame = Frame(window)
dosFrame.pack(side=BOTTOM, fill=X)

Uno = Label(unoFrame, text="Uno", bg="blue", fg="yellow") #Background color is bg, Foreground color if fg
Uno.pack(side=TOP)
Dos = Label(unoFrame, text="Dos", bg="black", fg="yellow")
Dos.pack(fill=X) #The point of this file: If you fill to X or Y, no matter how you resize the window the label will fill the space.
Tres = Label(unoFrame, text="Tres", bg="red", fg="yellow")
Tres.pack(side=LEFT, fill=Y)

#Just to show again with a button
button1 = Button(dosFrame,text="Button",fg="orange",bg="blue")
button1.pack(fill=X)
>>>>>>> 345b3f2e7875f835653cb665afcd81dd92486cdf
window.mainloop()
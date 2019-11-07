#This file is for Grid tutorial use. Grids are a much better method of organization, 
#especially if you have previously just been packing widgets in.
from tkinter import *
window = Tk()

unoLabel = Label(window,text="Name")
dosLabel = Label(window,text="Password")
#Entry is required for user input
unoEntry = Entry(window)
dosEntry = Entry(window)
#After creating these objects, where will we put them
unoLabel.grid(row=0, column=0, sticky=E) #column is redundant due to the column always being initalized at zero
dosLabel.grid(row=1, column=0, sticky=E) #sticky sticks the text to the side of the column. N(North) E(East) S(South) W(West)
#Then the entries will be placed next to the input labels
unoEntry.grid(row=0, column=1)
dosEntry.grid(row=1,column=1)
#How about a "Keep me logged in" checkbox?
cbox = Checkbutton(window, text="Keep me signed in")
cbox.grid(row=2,columnspan=2) #columnspan indicated how many columns this widget takes up

window.mainloop()
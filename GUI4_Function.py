#This file is for Function tutorial use. This is how to connect the widgets that have been formatted with your computer program.
from tkinter import *
window = Tk()
def name(): #This creates a function clled name() which will print "Samuel Lamb"
    print("Samuel Lamb")
button1 = Button(window,text="Press Me!",bg="red", command=name) #the command gives a purpose to this button, calling the name() function
button1.pack(fill=X) #Used pack to easily fill horixontal

def name_2(event): #event could be left click, right click, etc.
  print("Samuel Lamb 2.0")
button2 = Button(window,text="No! Press Me!",bg = "blue")
button2.bind("<Button-2>",name_2) #button-2 is middle mouse click, bind is an alternate to command (better)
button2.pack(fill=X)

def name_3(event): #event could be left click, right click, etc.
  print("Samuel Lamb 3.0")
button2 = Button(window,text="No! No! Press Me!",bg = "yellow")
button2.bind("<Button-3>",name_3) #button-3 is right click
button2.pack(fill=X) 

#binding allows for these different events with the functions. Say you want a button to do different things with each click:
def name_4(event):
    print("Left Click")
def name_5(event): 
  print("Middle Click")
def name_6(event):
  print("Right Click")
button4 = Button(window,text="Multi-Purpose",bg="purple")
button4.bind("<Button-1>",name_4) #If left clicked, "Left Click"
button4.bind("<Button-2>",name_5) #If Middle clicked, "Middle Click"
button4.bind("<Button-3>",name_6) #If Right clicked, "Right Click"
button4.pack(fill=X)
window.mainloop()
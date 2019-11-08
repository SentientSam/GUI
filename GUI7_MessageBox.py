#This file is a tutorial for the pop up message box in tkinter

from tkinter import *
import tkinter.messagebox #importing message box from tkinter library

window = Tk()
#tkinter.messagebox.showinfo("Samuel Lamb Message Box","This is a simple message")
survey = tkinter.messagebox.askquestion("Samuel Lamb Survey Box","Does this make sense?") #Title, and then the question
if survey == "yes":
  print("Glad to hear!")
else:
  print("That is a shame, check the code or message me!")
#you can implement this in many ways, it is just a cool thing to showcaseS
window.mainloop()
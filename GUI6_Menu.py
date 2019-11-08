#This file is to show menu functionality, focusing on the drop down menu
from tkinter import *
#first, to create something these buttons will do
def blank():
  print("Fill with a function bind") 

window = Tk()
#tkinter already has some menu functions and setting that do most of the work for you
mainMenu = Menu(window) #tkinter class Menu
window.config(menu=mainMenu) #config configured a menu using object "mainMenu"
dropMenu = Menu(mainMenu) #creating that first drop menu
mainMenu.add_cascade(label="File",menu=dropMenu) #adding an option to the main menu that is labeled "File" to initialize the first drop
dropMenu.add_command(label="Open",command=blank) #adding sub menu items
dropMenu.add_command(label="Save",command=blank)
dropMenu.add_separator() #seperator is super easy to use. required nothing
dropMenu.add_command(label="Exit",command=window.quit) #making the "Exit" button quit the loop, like in the classes file
#creating a second drop menu:
dropMenu_2 = Menu(mainMenu)
mainMenu.add_cascade(label="Edit",menu=dropMenu_2)
dropMenu_2.add_command(label="Nothing",command=blank)
dropMenu_2.add_separator()
dropMenu_2.add_checkbutton(label="Check") #a check button
#these drop menu options were based on vscode but you can have them as anything, even adding complex functions to the menu options.
window.mainloop()
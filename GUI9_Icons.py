#A file for adding images within tkinter

from tkinter import*
window = Tk()
picture = PhotoImage(file="GUI9_Icons.png")
displayLabel = Label(window, image = picture) # You cannot just display an image, you need to place it in a label
displayLabel.pack()
window.mainloop()
from tkinter import*
window = Tk()

Uno = Label(window, text="Uno", bg="blue", fg="yellow")
Uno.pack(side=TOP)
Dos = Label(window, text="Dos", bg="black", fg="yellow")
Dos.pack(fill=X)
Tres = Label(window, text="Tres", bg="red", fg="yellow")
Tres.pack(side=LEFT, fill=Y)
window.mainloop()
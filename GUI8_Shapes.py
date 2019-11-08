#This file will show how to use graphics and shapes in tkinter


from tkinter import *

window = Tk()

#need something to draw on, or a "canvas"
draw = Canvas(window,width = 300, height = 300) #(300 by 300 pixels)
draw.pack() #placing this object in the window

line_1 = draw.create_line(0,0,150,150) #starting position, ending position (pixels)
line_2 = draw.create_line(300,300,150,150,fill="blue") #line fill is == color
box_1 = draw.create_rectangle(50,50,250,250)
box_2 = draw.create_rectangle(75,75,225,225)

draw.delete() #whatever you put it in the paramter, it will delete as the loop goes on
#one simple implementation of the delete would be a button

# draw.delete(ALL) #Will erase the whole canvas

window.mainloop()
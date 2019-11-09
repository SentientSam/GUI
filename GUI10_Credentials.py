from tkinter import*

def write_File_1 (total):
    file = open("Note.txt", "a") #This function write_File will make a note.txt or take the one in the locations and add the input to it
    file.write('\n' + 'Service: ' + total.get() + '\n') #.get() takes the total variable (the input) and extracts the text from it
    file.close()
def write_File_2 (total):
    file = open("Note.txt", "a")
    file.write('Username: ' + total.get() + '\n')
    file.close()
def write_File_3 (total):
    file = open("Note.txt", "a")
    file.write('Password: ' + total.get() + '\n')
    file.close()

window = Tk()
#see label & grid tutorials if you need help with the formatting below
service = Label(window,text="Service:")
service.grid(row=1, column=1)
username = Label(window,text="Username:")
username.grid(row=2, column=1)
password = Label(window,text="Password:")
password.grid(row=3, column=1)

input_1 = Entry(window)
input_1.grid(row=1, column=2)
input_2 = Entry(window)
input_2.grid(row=2, column=2)
input_3 = Entry(window)
input_3.grid(row=3, column=2)

button_1 = Button( window , text = "Send to Note.txt" , command = lambda:[write_File_1(input_1),write_File_2(input_2),write_File_3(input_3)]).grid(row=4, columnspan=2, column=1)
#lambda is a service that allows for multiple functions to be assigned to one widget. I called all the functions I build to activate with the click of button_1

# Output would be: Service: <input_3>
#                  Username: <input_2>
#                  Password: <input_3>



window.mainloop()
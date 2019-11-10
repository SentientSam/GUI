# GUI
Tester files I am using to experiment with GUi and start developing

Graphical User Interfaces have become an interest of mine and I am hoping to experiment with them further and get to the point where I am comfortable developing.

The files here will be good introductory files. As I learn, I am going to comment these files and update them.

GUI.py is an intro file, showing frames, packing, buttons, and labels

GUI2.py is similar to GUI, however it shows some functionality of pack and further customizations

GUI3_Grid.py is where I started integrating the topic into the name (finally). It shows how to utilize grids, which are often superior to simply packing something into the window. Also shows a cool Checkbutton functionality.

GUI4_Function.py shows how to bind functions with widgets. Essentially this allows for buttins, etc. to actually perform an action. This file shows 2 methods of binding: The command parameter, and the bind function.

GUI5_Classes.py shows how classes are used with tkinter and also gives some insight into the exit button functionality and the init command function

GUI6_Menu.py is a menu file showing how to create and use a drop down menu. It does not go far into the uses of this but simply sshows the basics of "how to"

The second half of GUI6_Menu.py is showing how to make a toolbar and status bar (like in most applications)

GUI7_MessageBox.py showcases the message box in tkinter and how you can use it for various things. It is a pretty simple file but it can be very useful.

GUI8_Shapes.py is a small file showing how to make a canvas and shapes on the canvas. Also how to delte those shapes, etc.

GUI9_Icons.py is how to add images within tkinter.

GUI10_Credential.py is a personal project I wanted to work on that takes a service, username, and password input and posts those to a text file. It is fairly simple but showcases some useful tkinter applications. I often forget login credentials to some small sites and so this is a file I can easily pull up to store those is a secure space (after hashing)

For Any of these files you can use Pyinstaller to turn it into a .exe
To get pyinstaller, in your console type: pip install pyinstaller
After that you can either type: pyinstaller yourprogram.py
Or: pyinstaller.exe --onefile --icon=myicon.ico yourprogram.py
Where onefile simply ensures one file is created in dist and icon is where you can customize the executable icon.
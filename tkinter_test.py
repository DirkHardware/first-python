import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

# or

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+8+400")
#mainloop is what runs and controls all the methods

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='top', fill=tkinter.Y)

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.pack(side='top', anchor='e')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')

mainWindow.mainloop()

""" Everything in tkinter is a hierarchy of windows. Not all windows.
 Not all windows can have children but all windows except the root must
 have a parent. """
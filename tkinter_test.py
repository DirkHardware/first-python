import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

# or

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480")
#mainloop is what runs and controls all the methods
mainWindow.mainloop()
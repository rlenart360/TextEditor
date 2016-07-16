from tkinter import *
from tkinter import filedialog

def donothing():
	filewin = Toplevel(root)
	button = Button(filewin, text="Do nothing button")
	button.pack()

def open_file():
	textfield.delete("1.0", END)
	file2open = filedialog.askopenfile(mode='r')
	if file2open is None:
		return
	text2open = file2open.read()
	textfield.insert("1.0", text2open)
	
def save_input():
	file2save = filedialog.asksaveasfile(mode = 'w', defaultextension = ".txt")
	if file2save is None:
		return
	inputtext = str(textfield.get("1.0", END))
	file2save.write(inputtext)
	file2save.close()

def quit():
	root.destroy()

root = Tk()

frame = Frame(root, height=720, width=720)
frame.pack()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_input)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="About...", command=donothing)
helpmenu.add_command(label="Help Index", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

textfield = Text(frame)
textfield.pack()
textfield.place(x=10, y=10, height=700, width=700)

root.config(menu=menubar)
root.mainloop()

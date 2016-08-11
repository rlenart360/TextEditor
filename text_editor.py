from tkinter import *
from tkinter import filedialog

def draw_pixel(x, y, color):
	screen.create_rectangle(0+(x*16), 0+(y*16), 16+(x*16), 16+(y*16), fill=color)
	

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

frame = Frame(root, height=535, width=1244)
frame.pack()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_input)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Help", menu=helpmenu)

textfield = Text(frame, bg = "#a5c0c9")
textfield.pack()
textfield.place(x=10, y=10, height=510, width=700)

screen = Canvas(frame, bg = "black")
screen.pack()
screen.place(x=720, y=10, height=512, width=512)
#draw_pixel(10,30,'red')


root.config(menu=menubar)
root.mainloop()

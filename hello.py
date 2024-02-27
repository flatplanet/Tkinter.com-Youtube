from tkinter import *

root = Tk()
root.title("Hello World!!")
root.iconbitmap('images/tkinter.ico')
root.geometry('500x350')

# Create global switch variable
global switch
switch = True
def change():
	global switch
	if switch == True:
		my_label.config(text="Goodbye World!")
		switch = False
	else:
		my_label.config(text="Hello World!")
		switch = True


# Create a Label
my_label = Label(root, text="Hello World!", font=("Helvetica", 24))
# Pack, Grid, Place
my_label.pack(pady=20)

# Create a Button
my_button = Button(root, text="Click Me!", font=("Helvetica", 16), command=change)
my_button.pack(pady=20)














root.mainloop()


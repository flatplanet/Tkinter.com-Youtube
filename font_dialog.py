from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import FontDialog

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Font Dialog!")
root.iconbitmap('images/codemy.ico')
root.iconbitmap(default='images/codemy.ico')
root.geometry('300x200')

def open_font():
	# Define Font Dialog
	fd = FontDialog(bootstyle="danger")
	# Show the box
	fd.show()
	# Capture The Reult fd.result and update label
	my_label.config(font=fd.result)


# Create a label and button
my_button = tb.Button(root, text="Open Font Dialog", command=open_font)
my_button.pack(pady=40)

my_label = tb.Label(root, text="Hello World!")
my_label.pack(pady=10)


root.mainloop()
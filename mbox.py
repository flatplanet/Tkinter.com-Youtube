from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Message Box")
# Main App Icon
root.iconbitmap('images/codemy.ico')
# Message Box Icon
root.iconbitmap(default='images/codemy.ico')
root.geometry('700x350')

def clicker():
	# create a dialog
	# yesno, ok, okcancel, show_info, show_error, show_question
	# show_warning, yesnocancel, retrycancel
	mb = Messagebox.retrycancel("Display Some Message Here", "Here is the Title")

	#if mb == "No":
	#	print("no")
	#else:
	#	print("yes")
	
	# Display button click
	my_label.config(text=f'You Clicked {mb}')


my_button = tb.Button(root, text="Click Me!", bootstyle='danger', command=clicker)
my_button.pack(pady=40)

my_label = tb.Label(root, text='', font=("Helvetica", 18))
my_label.pack(pady=20)



root.mainloop()
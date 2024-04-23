from tkinter import *

root = Tk()
root.title("Status Bars - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

global count
count=1
def next():
	global count
	my_status.config(text=f"{count} of 100  ")
	count +=1

my_button = Button(root, text="Next >>", command=next, font=("Helvetica", 24))
my_button.pack(pady=100)

# Create our status bar
my_status = Label(root, text="0 of 100  ", anchor=E, relief="sunken", bd=1) # raised, sunken, flat, ridge, groove
my_status.pack(side="bottom", fill="x", ipady=2)




root.mainloop()


from tkinter import *

root = Tk()
root.title("Status Bars - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

global count
count = 1
def next():
	global count
	my_status.config(text=f"{count} of 100  ")
	#increment the counter
	count += 1
	


my_button = Button(root, text="Next >>", font=("Helvetica", 18), command=next)
my_button.pack(pady=100)

# Create a status bar
my_status = Label(root, text="0 of 100  ", anchor=E, relief="sunken", bd=1) # flat, sunken, raised, groove, ridge
my_status.pack(fill="x", side="bottom", ipady=2)



root.mainloop()


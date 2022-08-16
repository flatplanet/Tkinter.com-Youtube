from tkinter import *

# Define Our Main Screen
root = Tk()
root.title('Tkinter.com - Button Widget!')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("500x350")

def clicker():
	my_button.config(text="You Clicked The Button!")
	my_button.config(width="19")	

#Define an Image
login = PhotoImage(file='images/login.png')

my_button = Button(root, text="Click Me!",
	activebackground="black",
	activeforeground="red",
	anchor="center",
	bg="systembuttonface",
	bd="2",
	command=clicker,
	default="disabled",
	disabledforeground="green",
	font=("Helvetica", 32),
	fg="blue",
	#height="10",
	#highlightbackground="blue",
	#highlightcolor="red",
	#image=login,
	justify="center",
	overrelief="raised",
	relief="raised",
	state="normal",
	takefocus=TRUE,
	underline=3,
	width="10",
	wraplength="0"
	)
my_button.pack(pady=50)




# Create The Mainloop That All Apps Need
root.mainloop()
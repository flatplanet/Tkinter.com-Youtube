from tkinter import *


root = Tk()
root.title('Tkinter.com - Button Widget!')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("500x350")

login = PhotoImage(file="images/login.png")

# 23 Attributes
my_button = Button(root, text="Click Me! ",
	#activebackground="",
	#activeforeground="",
	#anchor="",
	#bg="",
	#bd="",
	#command="",
	#default="",
	#disabledforeground="",
	font=("Halvetica", 32),
	#fg="",
	#height="",
	#highlightbackground="",
	#highlightcolor="",
	#image=,
	#justify="",
	#overrelief="",
	#relief="",
	#state="",
	#takefocus="",
	#underline="",
	#width="",
	#wraplength=""
	)

my_button.pack(pady=50)


root.mainloop()
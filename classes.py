from tkinter import *


class App(Tk):
	def __init__(self):
		super().__init__()

		# Title, icon, size
		self.title("Tkinter.com - Object Oriented Programming!")
		self.iconbitmap('images/codemy.ico')
		self.geometry('700x450')

		# Create Status Variable
		self.status = True

		# Create some widgets
		self.my_label = Label(self, text="Hello World!", font=("Helvetica", 42))
		self.my_label.pack(pady=20)

		self.my_button = Button(self, text="Change Text", command=self.change)
		self.my_button.pack(pady=20)

		# Create a frame outside this function
		My_frame(self)

	def change(self):
		if self.status == True:
			self.my_label.config(text="Goodbye World!")
			self.status = False
		else:
			self.my_label.config(text="Hello World!")
			self.status = True

class My_frame(Frame):
	def __init__(self, parent):
		super().__init__(parent)

		# Put this sucker on the screen
		self.pack(pady=20)
		# Create a few buttons
		self.my_button1 = Button(self, text="Change", command=parent.change)
		self.my_button2 = Button(self, text="Change", command=parent.change)
		self.my_button3 = Button(self, text="Change", command=parent.change)

		self.my_button1.grid(row=0, column=0, padx=10)
		self.my_button2.grid(row=0, column=1, padx=10)
		self.my_button3.grid(row=0, column=2, padx=10)




# Define and instantiate our app
app = App()
app.mainloop()
from tkinter import *
from tkinter import messagebox

class App(Tk):
	def __init__(self):
		super().__init__()

		# Title, icon, size
		self.title("Tkinter.com - OOP Popup Boxes")
		self.iconbitmap('images/codemy.ico')
		self.geometry('700x450')

		# Create Widgets
		self.my_label = Label(self, text="Enter Your Name:", 
			font=("Helvetica", 24))
		self.my_label.pack(pady=20)

		self.my_entry = Entry(self, width=30, font=("Helvetica", 24))
		self.my_entry.pack(pady=20)

		self.my_button = Button(self, text="Popup", command=self.popup)
		self.my_button.pack(pady=20)
	
	# Create Popup Function
	def popup(self):
		#showinfo()
		#showwarning()
		#showerror ()
		#askquestion()
		#askokcancel()
		#askyesno ()
		#askretrycancel ()
		if self.my_entry.get():
			messagebox.showinfo("Hello", f"Hello {self.my_entry.get()}")
		else:
			messagebox.showerror("Error", "You Forgot To Type In Your Name!! Try Again")

# Define and instantiate our app
app = App()
app.mainloop()
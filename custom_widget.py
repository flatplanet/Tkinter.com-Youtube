from tkinter import *

root = Tk()
root.title('Tkinter.com - Custom Widgets/Components')
root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

class My_widget(Frame):
	def __init__(self, parent, label_text, button_text, button_name):
		super().__init__(master = parent)

		# Set up our grid stuff
		self.rowconfigure(0, weight=1)
		self.columnconfigure((0,1), weight=1, uniform='z')

		# Create our widgets
		Label(self, text=label_text, font=("Helvetica", 18)).grid(row=0, column=0, sticky="nsew")
		Button(self, text=button_text, command=lambda: self.change(button_name)).grid(row=0, column=1, sticky="nsew")

		self.pack(expand=True, fill="both", padx=10, pady=10)

	def change(self, name):
		if name == "my_button1":
			root.title("Button 1!")
		elif name == "my_button2":
			root.title("Button 2!")
		elif name == "my_button3":
			root.title("Button 3!")
		else:
			root.title("Something else!")


My_widget(root, "Text 1", "Button 1", "my_button1")
My_widget(root, "Text 2", "Button 2", "my_button2")
My_widget(root, "Text 3", "Button 3", "my_button3")
My_widget(root, "Text 4", "Button 4", "my_button4")


root.mainloop()
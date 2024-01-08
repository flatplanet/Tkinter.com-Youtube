from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		#root = customtkinter.CTk()

		self.title('Tkinter.com - Object Oriented CustomTkinter')
		self.iconbitmap('images/codemy.ico')
		self.geometry('700x450')


		

		# Text Box
		self.my_text = customtkinter.CTkTextbox(self, width=600, height=300)
		self.my_text.pack(pady=20)

		self.my_button = customtkinter.CTkButton(self, text="Clear Box", command=self.clear)
		self.my_button.pack(pady=20)

	def clear(self):
		self.my_text.delete('0.0', END)

# Define app and Create our app's mainloop
app = App()
app.mainloop()
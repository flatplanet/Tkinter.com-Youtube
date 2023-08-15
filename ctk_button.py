from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Buttons')
root.iconbitmap('images/codemy.ico')
root.geometry('600x350')

def hello():
	my_label.configure(text=my_button.cget("text"))



my_button = customtkinter.CTkButton(root, 
	text="Hello World!!!", 
	command=hello,
	height=100,
	width=200,
	font=("Helvetica", 24),
	text_color="black",
	fg_color="red",
	hover_color="green",
	corner_radius=50,
	bg_color="white",
	border_width=10,
	border_color="yellow",
	state="normal")
my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)




root.mainloop()
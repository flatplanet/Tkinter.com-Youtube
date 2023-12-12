from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Light Dark Modes')
root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

mode = "dark"

def change_colors(choice):
	customtkinter.set_default_color_theme(choice)

def change():
	global mode
	if mode == "dark":
		customtkinter.set_appearance_mode("light")
		mode = "light"
		# Clear text box
		my_text.delete(0.0, END)
		my_text.insert(END, "This is Light Mode...")
	else:
		customtkinter.set_appearance_mode("dark")
		mode = "dark"
		# Clear text box
		my_text.delete(0.0, END)
		my_text.insert(END, "This is Dark Mode...")


my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)
my_button.pack(pady=20)

colors = ["blue", "dark-blue", "green"]
my_option = customtkinter.CTkOptionMenu(root, values=colors, command=change_colors)
my_option.pack(pady=10)







root.mainloop()

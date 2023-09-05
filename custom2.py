from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter!')
root.iconbitmap('images/codemy.ico')
root.geometry('700x450')


def game():
	if check_var.get() == "on":
		my_label.configure(text="Excellant! Let's Play!")	
	else:
		my_label.configure(text="Are You Sure You Don't Want To Play?")

def clear():
	my_check.deselect()	

def toggle2():
	my_check.toggle()

check_var = customtkinter.StringVar(value="off")
my_check = customtkinter.CTkCheckBox(root, text="Would You Like To Play A Game?", 
	variable=check_var, onvalue="on", offvalue="off",
	checkbox_width=50,
	checkbox_height=50,
	#corner_radius=50,
	#fg_color="red",
	#border_color="red",
	#hover_color="red",
	#text_color="red", 
	hover=True,
	font=("helvetica", 18),
	)
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Submit", command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack(pady=20)

toggle_button = customtkinter.CTkButton(root, text="Toggle Checkbox", command=my_check.toggle)
toggle_button.pack(pady=20)

# select() and .deselect()

my_label = customtkinter.CTkLabel(root, text="", font=("helvetica", 18))
my_label.pack(pady=20)

root.mainloop()

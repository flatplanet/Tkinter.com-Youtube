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
		my_label.configure(text="You Clicked the thing!")
	else:
		my_label.configure(text="You Didn't Click the thing!")

	text_var.set("Awesome!!")
	

def clear_me():
	my_check.deselect()
	text_var.set("Would You Like To Play A Game?")

# Checkbox state
check_var = customtkinter.StringVar(value="off")
# Checkbox Text
text_var = customtkinter.StringVar(value="Would You Like To Play A Game?")
my_check = customtkinter.CTkCheckBox(root, text="Would You Like To Play A Game?",
	variable=check_var, onvalue="on", offvalue="off",
	checkbox_width=50,
	checkbox_height=50,
	font=("helvetica", 18),
	corner_radius=50,
	fg_color="red",
	hover_color="green",
	text_color="red",
	hover=False,
	textvariable=text_var,
	)
my_check.pack(pady=40)


my_button = customtkinter.CTkButton(root, text="Submit", command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear_me)
clear_button.pack(pady=10)

toggle_button = customtkinter.CTkButton(root, text="Toggle", command=my_check.toggle)
toggle_button.pack(pady=10)

select_button = customtkinter.CTkButton(root, text="Select", command=my_check.select)
select_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)



root.mainloop()

from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Radio Buttons!')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

def get_rad():
	if radio_var.get() == "other":
		my_label2.configure(text="Please Make A Selection")
	elif radio_var.get() == "Yes":
		my_label2.configure(text="Of Course You Like Pizza!")
	else:
		my_label2.configure(text="What's Wrong With You?!")

my_label = customtkinter.CTkLabel(root, text="Do You Like Pizza?!", font=("Helvetica", 18))
my_label.pack(pady=40)

radio_var = customtkinter.StringVar(value="other")
# Radio Button 1
my_rad1 = customtkinter.CTkRadioButton(root, text="Yes I Do", value="Yes", 
	variable=radio_var,
	#width=50,
	#height=50,
	radiobutton_width=50,
	radiobutton_height=50,
	corner_radius=1,
	border_width_unchecked = 2,
	border_width_checked=5,
	border_color="red",
	hover_color="pink",
	fg_color="green",
	hover=True,
	text_color="red",
	font=("Helvetica", 18),
	state="normal",
	text_color_disabled="green"



	)
my_rad1.pack(pady=10)
# Radio Button 2
my_rad2 = customtkinter.CTkRadioButton(root, text="No I Don't", value="No", 
	variable=radio_var,
	)
my_rad2.pack(pady=10)

# Button
my_button = customtkinter.CTkButton(root, text="Select", command=get_rad)
my_button.pack(pady=10)

# Label
my_label2 = customtkinter.CTkLabel(root, text="", font=("Helvetica",18))
my_label2.pack(pady=10)











root.mainloop()

from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Switch')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

# Create Function
def switcher():
	my_label.configure(text=switch_var.get())

# Create Toggle function
def clicker():
	#my_switch.deselect()
	#my_switch.select()
	my_switch.toggle()

# Create a StringVar
switch_var = customtkinter.StringVar(value="on")
# Create Switch
my_switch = customtkinter.CTkSwitch(root, text="Switch", command=switcher,
	variable=switch_var, onvalue="on", offvalue="off",
	#width=200,
	#height=100,
	switch_width=200,
	switch_height=25,
	#corner_radius=10,
	border_color="orange",
	border_width=5,
	fg_color="red",
	progress_color="green",
	button_color="pink",
	button_hover_color="yellow",
	font=("Helvetica", 24),
	text_color="blue",
	state="normal",

	)
my_switch.pack(pady=40)


# Create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

# Create Button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=clicker)
my_button.pack(pady=10)

root.mainloop()

from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter ComboBox')
root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

def color_picker(choice):
	output_label.configure(text=choice, text_color=choice)

def color_picker2():
	output_label.configure(text=my_combo.get(), text_color=my_combo.get())	

def color_picker_yellow():
	# Set the combo box option
	my_combo.set("Yellow")
	output_label.configure(text=my_combo.get(), text_color=my_combo.get())		

my_label = customtkinter.CTkLabel(root, text="Pick A Color", font=("Helvetica", 18))
my_label.pack(pady=40)

# Set the options for our combobox
colors = ["Red", "Green", "Blue"]
# Create combobox
my_combo = customtkinter.CTkComboBox(root, values=colors,
	height=50,
	width=200,
	font=("Helvetica", 18),
	dropdown_font=("Helvetica", 18),
	corner_radius=50,
	border_width=2,
	border_color="red",
	button_color="red",
	button_hover_color = "green",
	dropdown_hover_color = "green",
	dropdown_fg_color = "blue",
	dropdown_text_color="orange",
	text_color="silver",
	hover=True,
	justify="center",
	state="normal" # normal
	)
my_combo.pack(pady=0)

# Create A Button
my_button = customtkinter.CTkButton(root, text="Pick A Color", command=color_picker2)
my_button.pack(pady=20)

# Yellow button
yellow_button = customtkinter.CTkButton(root, text="Pick Yellow!", command=color_picker_yellow)
yellow_button.pack(pady=20)

# Create output label
output_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
output_label.pack(pady=20)


root.mainloop()

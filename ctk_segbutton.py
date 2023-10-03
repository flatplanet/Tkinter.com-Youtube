from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Scrollable Frame!')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

# Create our function
def clicker(value):
	my_label.configure(text=f'Hello {value}')

# Our button values
my_values = ["John", "April", "Wes"]
# Create the button
my_seg_button = customtkinter.CTkSegmentedButton(root, values=my_values, command=clicker,
	width=300,
	height=100,
	font=("Helvetica",58),
	corner_radius=3,
	border_width=5,
	fg_color="red",
	selected_color="green",
	selected_hover_color="purple",
	unselected_color="pink",
	unselected_hover_color="orange",
	text_color="yellow",
	state="normal",
	text_color_disabled="blue",
	dynamic_resizing=True
	)


my_seg_button.pack(pady=40)

# Set default Selection
#my_seg_button.set("John")

# Label
my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()

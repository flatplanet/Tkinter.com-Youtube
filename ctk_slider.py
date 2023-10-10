from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Slider')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

# Function
def sliding(value):
	my_label.configure(text=int(value))


my_slider = customtkinter.CTkSlider(root, 
	from_=0,
	to=100,
	command=sliding,
	orientation="horizontal",
	number_of_steps=10,
	width=400,
	height=50,
	#border_width=100,
	fg_color="red",
	progress_color="green",
	button_color="yellow",
	button_hover_color="orange",
	state="normal",
	hover=False



	)

my_slider.pack(pady=40)

# Define starting point
my_slider.set(0)

my_label = customtkinter.CTkLabel(root, text=my_slider.get(), font=("Helvetica", 18))
my_label.pack(pady=20)



root.mainloop()

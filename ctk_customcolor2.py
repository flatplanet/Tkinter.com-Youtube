from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("themes/red.json")  # Themes: blue (default), dark-blue, green
# Turn off scaling
customtkinter.deactivate_automatic_dpi_awareness()
# Scale Window
customtkinter.set_window_scaling(1.5)
# Scale Widgets
customtkinter.set_widget_scaling(1.5) 

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Custom Color Themes')
root.iconbitmap('images/codemy.ico')
root.geometry('700x550')

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

my_progress = customtkinter.CTkProgressBar(root, orientation="horizontal")
my_progress.pack(pady=20)





root.mainloop()

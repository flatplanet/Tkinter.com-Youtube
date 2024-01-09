from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Widget Animations')
root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

global my_y
my_y = 450/2+350

def up():
	global my_y
	my_y -= 20
	if my_y >= 195:
		my_text.place(x=700/2, y=my_y, anchor='center')
		up_button.configure(text=my_y)
		root.after(5, up)

def down():
	global my_y
	my_y += 20
	if my_y <= 750:
		my_text.place(x=700/2, y=my_y, anchor='center')
		up_button.configure(text=my_y)
		root.after(5, down)


#Frame
my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=20)

# Buttons
up_button = customtkinter.CTkButton(my_frame, text="Up", command=up)
up_button.grid(row=0, column=0, padx=10)

down_button = customtkinter.CTkButton(my_frame, text="Down", command=down)
down_button.grid(row=0, column=1, padx=10)

# Text Box 
my_text = customtkinter.CTkTextbox(root, width=400, height=200)
my_text.place(x=700/2, y=my_y, anchor='center')



root.mainloop()
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter.font import Font



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Todo List')
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry("500x300")

# Define Our Images
#add_folder_image = ImageTk.PhotoImage(Image.open("images/add-folder.png").resize((20,20), Image.ANTIALIAS))
#add_list_image = ImageTk.PhotoImage(Image.open("images/add-list.png").resize((20,20), Image.ANTIALIAS))


# Define our Font
my_font = Font(
	family="Brush Script MT",
	size=30,
	weight="bold")

# Creat frame
my_frame = customtkinter.CTkFrame(root, corner_radius=20)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
	font=my_font,
	width=25,
	height=5,
	bg="black",
	bd=0,
	fg="#464646",
	highlightthickness=0,
	selectbackground="#a6a6a6",
	activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)







# Create Our Buttons
button_1 = customtkinter.CTkButton(master=root, text="Add Folder", width=190, height=40, compound="top")
button_1.pack(pady=20, padx=20)

button_2 = customtkinter.CTkButton(master=root, text="Add Item", width=190, height=40, compound="right", 
	fg_color="#D35B58", hover_color="#C77C78")
button_2.pack(pady=10, padx=20)	



root.mainloop()
from tkinter import *
import customtkinter
from PIL import Image


customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Images')
root.iconbitmap('images/codemy.ico')
root.geometry('400x550')


my_image = customtkinter.CTkImage(light_image=Image.open('images/aspen1.png'),
	dark_image=Image.open('images/aspen1.png'),
	size=(180,250)) # WidthxHeight

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)



root.mainloop()

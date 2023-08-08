from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter!')
root.iconbitmap('images/codemy.ico')
root.geometry('600x350')


my_button = customtkinter.CTkButton(root, text="Hello World!!!")
my_button.pack(pady=80)




root.mainloop()
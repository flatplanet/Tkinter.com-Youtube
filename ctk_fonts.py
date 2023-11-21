from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Fonts')
root.iconbitmap('images/codemy.ico')
root.geometry('400x200')

def change():
	my_font.configure(underline=False, overstrike=False, size=22, slant="roman")

my_font = customtkinter.CTkFont(family="Helvetica", size=44, 
	weight="bold", slant="italic", underline=True, overstrike=True) #weight bold/normal, slant=italic/roman

my_label = customtkinter.CTkLabel(root, text="This is Text", font=my_font)
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Change Text", command=change)
my_button.pack()



root.mainloop()

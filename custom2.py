from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter!')
root.iconbitmap('images/codemy.ico')
root.geometry('700x350')

def submit():
	my_label.configure(text=f'Hello {my_entry.get()}')

def clear():
	my_entry.delete(0,END)

my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root, placeholder_text="Enter Your Name",
width=200,
height=50,
corner_radius=50,
text_color="green",
placeholder_text_color="black",
#fg_color=("blue", "lightblue"), # outer, inner
font=("Helvetica", 18),
#state="disabled", # or normal
)
my_entry.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Submit", command=submit)
my_button.pack(pady=10)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear)
clear_button.pack()



root.mainloop()


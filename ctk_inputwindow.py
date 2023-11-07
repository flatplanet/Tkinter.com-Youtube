from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Input Window')
root.iconbitmap('images/codemy.ico')
root.geometry('400x200')

# Create Function
def input():
	dialog = customtkinter.CTkInputDialog(text="What is your Name?", title="Hello There!",
		fg_color="white",
		button_fg_color="red",
		button_hover_color="pink",
		button_text_color="black",
		entry_fg_color="green",
		entry_border_color="red",
		entry_text_color="black"


		)
	thing = dialog.get_input()
	if thing:
		my_label.configure(text=f"Hello {thing}")
	else:
		my_label.configure(text=f"You Forgot To Type Anything!")



# Create a Button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=input)
my_button.pack(pady=40)

# Create a Label
my_label = customtkinter.CTkLabel(root, text='')
my_label.pack(pady=10)





root.mainloop()

from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter TextBox')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

thing = ''

# Functions
def delete():
	my_text.delete(0.0, 'end')

def copy():
	global thing
	thing = my_text.get(0.0, 'end')

def paste():
	if thing:
		my_text.insert('end', thing)
	else:
		my_text.insert('end', "There is nothing to paste!!")


my_text = customtkinter.CTkTextbox(root,
	width=600,
	height=200,
	corner_radius=1,
	border_width=10,
	border_color="#003660",
	border_spacing=10,
	fg_color="silver",
	text_color="black",
	font=("Helvetica", 18),
	wrap="word", # Char default, word, none
	activate_scrollbars = True,
	scrollbar_button_color="blue",
	scrollbar_button_hover_color="red",

	)
my_text.pack(pady=20)


my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=10)
paste_button.grid(row=0, column=2)




root.mainloop()

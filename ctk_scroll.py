from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - Custom Tkinter Scrollable Frame!')
root.iconbitmap('images/codemy.ico')
root.geometry('700x300')

# Create a scrollable frame
my_frame = customtkinter.CTkScrollableFrame(root,
	orientation="vertical",
	width=300,
	height=200,
	label_text="Hello World!",
	label_fg_color="blue",
	label_text_color="yellow",
	label_font=("Helvetica", 18),
	label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
	border_width=3,
	border_color="green",
	fg_color="red",
	scrollbar_fg_color="yellow",
	scrollbar_button_color="pink",
	scrollbar_button_hover_color = "blue",
	corner_radius = 20,








	)
my_frame.pack(pady=40)


# for loop for buttons
for x in range(20):
	customtkinter.CTkButton(my_frame, text="This is a Button!!").pack(pady=10)







root.mainloop()

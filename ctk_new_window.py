from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter New Toplevel Window')
root.iconbitmap('images/codemy.ico')
root.geometry('400x200')

def new():
	new_window = customtkinter.CTkToplevel(root, fg_color="white")
	new_window.title("This is a new window!")
	new_window.geometry("400x200")
	new_window.resizable(False, True) # Width, Height


	def close():
		new_window.destroy()
		new_window.update()


	# Close the window
	new_button = customtkinter.CTkButton(new_window, text="Close Window", command=close)
	new_button.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Open New Window", command=new)
my_button.pack(pady=40)





root.mainloop()

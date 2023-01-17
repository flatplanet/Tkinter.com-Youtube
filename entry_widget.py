from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Combobox")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Create Entry Function
def speak():
	my_label.config(text=f'You Typed: {my_entry.get()}')

# Create Entry Widget
# Colors: primary, secondary, success, info, warning, danger, light, dark
my_entry = tb.Entry(root, bootstyle="success", 
	font=("Helvetica", 18),
	foreground="green",
	width=15,
	show="&")
my_entry.pack(pady=50)


# Create Button
my_button = tb.Button(root, bootstyle="danger outline", text="Click Me", command=speak)
my_button.pack(pady=20)


# Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
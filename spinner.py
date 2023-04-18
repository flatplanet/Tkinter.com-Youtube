from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Spinbox")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

def spinny():
	my_label.config(text=my_spin.get())


# Spinbox list
stuff = ["John", "April", "Bob", "Mary"]

# Spinbox!!
my_spin = tb.Spinbox(root, bootstyle="success", font=("Helvetica",18),
	from_=0, to=10, values=stuff, state="readonly",
	command=spinny)
my_spin.pack(pady=20)

# Set spinbox default
my_spin.set("John")

# Button
my_button = tb.Button(root, text="Click Me!", bootstyle="success", command=spinny)
my_button.pack(pady=20)

# Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()
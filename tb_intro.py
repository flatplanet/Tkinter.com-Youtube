from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')


# Create a Function for the Button
counter = 0
def changer():
	global counter
	counter += 1
	if counter % 2 == 0:
		my_label.config(text="Hello World!")
	else:
		my_label.config(text="Goodbye World!")




# Colors:
# Default, primary, secondary, success, info, warning, danger, 
# light, dark


# Create a Label
my_label = tb.Label(text="Hello World!", font=("Helvetica", 28), 
	bootstyle="danger, inverse")
my_label.pack(pady=50)

# Create a Button
my_button = tb.Button(text="Click Me!", 
	bootstyle="success, outline", command=changer)
my_button.pack(pady=20)


root.mainloop()
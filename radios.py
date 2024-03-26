from tkinter import *


root = Tk()
root.title("Radio Buttons - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

# Create our clicked function
def clicked():
	my_label.config(text=f'You Picked {radvar.get()}!')

# Create button function
def selector():
	radvar.set("Mushroom")
	clicked()

# Make function
def make():
	my_label.config(text=f'You Picked {radvar.get()}!')

# Create a Tkinter Var (IntVar, StringVar)
radvar = StringVar()

# Create our radio buttons
radio1 = Radiobutton(root, text="Pepperoni", variable=radvar, value="Pepperoni", command=clicked)
radio1.pack(pady=(40, 10))

radio2 = Radiobutton(root, text="Cheese", variable=radvar, value="Cheese", command=clicked)
radio2.pack(pady=(40, 10))

radio3 = Radiobutton(root, text="Mushroom", variable=radvar, value="Mushroom", command=clicked)
radio3.pack(pady=(40, 10))

# Set default radio button
radvar.set("Pepperoni")



my_label = Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)


# Button
my_button = Button(root, text="Select Mushroom", command=selector)
my_button.pack(pady=10)

my_button2 = Button(root, text="Make Selection", command=make)
my_button2.pack(pady=10)



root.mainloop()


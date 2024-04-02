from tkinter import *


root = Tk()
root.title("CheckButtons - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')


def clicked():
	# Check for pepperoni
	if var1.get() == 1:
		pepperoni = "Pepperoni"
	else:
		pepperoni = ""

	# Check for cheese
	if var2.get() == 1:
		cheese = "Cheese"
	else:
		cheese = ""

	# Check for mushroom
	if var3.get() == 1:
		mushroom = "Mushroom"
	else:
		mushroom = ""

	if pepperoni or cheese or mushroom:
		my_label.config(text=f"You Selected {pepperoni} {cheese} {mushroom}")
	else:
		my_label.config(text="You Didn't Pick Anything!")

# Create some IntVars()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# Create 3 checkboxes
check1 = Checkbutton(root, text="Pepperoni", variable=var1, onvalue=1, offvalue=0, font=("Helvetica", 18))
check1.pack(pady=(40, 10))

check2 = Checkbutton(root, text="Cheese", variable=var2, onvalue=1, offvalue=0, font=("Helvetica", 18))
check2.pack(pady=(40, 10))


check3 = Checkbutton(root, text="Mushroom", variable=var3, onvalue=1, offvalue=0, font=("Helvetica", 18))
check3.pack(pady=(40, 10))

# Create a button
my_button = Button(root, text="Submit", command=clicked)
my_button.pack(pady=20)


# Create a label
my_label = Label(root, text="Pick A Topping", font=("Helvetica", 18))
my_label.pack(pady=20)


root.mainloop()


from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Radio Buttons")
root.iconbitmap('images/codemy.ico')
root.geometry('500x550')

# Clicker Function
def clicker():
	my_label.config(text=f'You Selected: {my_topping.get()}')


# Create Radio Button List
toppings = ["Pepperoni", "Cheese", "Veggie"]

# Create A Tkinter Variable To Keep Track of everything
my_topping = StringVar()

# Loop thru the list and create radio buttons
for topping in toppings:
	tb.Radiobutton(root, bootstyle="danger", variable=my_topping, text=topping, value=topping, command=clicker).pack(pady=20)

# Create button
my_button = tb.Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=20)

# Create a Label 
my_label = tb.Label(root, text="You Selected: ")
my_label.pack(pady=20)

# Create actual Radio Button Buttons
rb1 = tb.Radiobutton(root, bootstyle="info toolbutton", variable=my_topping, text="Radio Button 1", value="Radio Button 1", command=clicker)
rb1.pack(pady=20)

rb2 = tb.Radiobutton(root, bootstyle="info toolbutton outline", variable=my_topping, text="Radio Button 2", value="Radio Button 2", command=clicker)
rb2.pack(pady=20)

root.mainloop()
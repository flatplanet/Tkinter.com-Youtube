from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ComboBoxes - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

def submit():
	my_label.config(text=my_combo.get())
	#my_combo.set("Cheese")

	# Output the whole list
	#items=""
	#for thing in my_combo['values']:
	#	items = items + thing + "\n"
	#my_label.config(text=items)

# Create a ComboBox
my_list = ["Peperroni", "Cheese", "Mushroom"]
my_combo = ttk.Combobox(root, values=my_list, state="readonly", width=20, font=("Helvetica", 18))
my_combo.pack(pady=20)

# set default item
my_combo.set("Peperroni")


my_label = Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

my_button = Button(root, text="Submit", command=submit)
my_button.pack(pady=20)


root.mainloop()


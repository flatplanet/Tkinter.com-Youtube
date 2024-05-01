from tkinter import *

root = Tk()
root.title("Menu Button Popups - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

def thing(item):
	my_label.config(text=f'You Cliked {item}')


# Create a menu button
my_menu = Menubutton(root, text="File Menu", relief="raised") # flat, sunken, raised, groove, ridge
my_menu.pack(pady=100)

# Define the menu
my_menu.menu = Menu(my_menu, tearoff=0)
my_menu["menu"] = my_menu.menu

# Add sub items
my_menu.menu.add_command(label="New", command=lambda: thing("New")) 
my_menu.menu.add_checkbutton(label="Open", command=lambda: thing("Open"))
my_menu.menu.add_radiobutton(label="Save", command=lambda: thing("Save"))
my_menu.menu.add_radiobutton(label="Save As", command=lambda: thing("Save As"))


# Add a label
my_label = Label(root, text="", font=("Helvetica", 24))
my_label.pack()

root.mainloop()


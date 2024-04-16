from tkinter import *

root = Tk()
root.title("Menus - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

def thing(whatever):
	my_label.config(text=whatever)

# Create our main menu
my_menu = Menu(root)

# Create a category item for your menu
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)

# Add sub-items to our File_Menu 
file_menu.add_command(label="New", command=lambda: thing("New"))
file_menu.add_command(label="Open", command=lambda: thing("Open"))
file_menu.add_command(label="Save", command=lambda: thing("Save"))
# Add a separator
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add another Category Item
edit_menu = Menu(my_menu, tearoff=1)
my_menu.add_cascade(label="Edit", menu=edit_menu)

# Add sub item to edit menu
edit_menu.add_command(label="Cut", command=lambda: thing("Cut"))
edit_menu.add_command(label="Copy", command=lambda: thing("Copy"))
edit_menu.add_command(label="Paste", command=lambda: thing("Paste"))
edit_menu.add_checkbutton(label="Checkbox", command=lambda: thing("Check"))
edit_menu.add_radiobutton(label="RadioButton 1", command=lambda: thing("Radio 1"))
edit_menu.add_radiobutton(label="RadioButton 2", command=lambda: thing("Radio 2"))












# Initialize the menu
root.config(menu=my_menu)

my_label = Label(root, text="Select From Menu Above", font=("Helvetica", 24))
my_label.pack(pady=100)





root.mainloop()


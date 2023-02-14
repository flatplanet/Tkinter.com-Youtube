from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Menu Button!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

def stuff(x):
	my_menu.config(bootstyle=x)
	my_label.config(text=f'You Selected {x}')


my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=50)

# Create basic menu
inside_menu = tb.Menu(my_menu)

# Add Items To Our Inside Menu
item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary', 'outline danger', 'outline info']:
	inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

# Associate the inside menu with the menubutton
my_menu['menu'] = inside_menu

# Create a label
my_label = tb.Label(root, text="")
my_label.pack(pady=40)


root.mainloop()

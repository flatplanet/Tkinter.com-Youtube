from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Treeview")
root.iconbitmap('images/codemy.ico')
root.geometry('700x350')

# Define Columns
columns = ("first_name", "last_name", "email")

# Create Treeview
my_tree = tb.Treeview(root, bootstyle="danger", columns=columns, 
	show="headings")
my_tree.pack(pady=20)

# Define headings
my_tree.heading('first_name', text="First Name")
my_tree.heading('last_name', text="Last Name")
my_tree.heading('email', text="Email Address")

# Create Sample Data
contacts = []

for n in range(1,20):
	contacts.append((f'First {n}', f'Last {n}', f'email{n}@address.com'))

# Add Data To Treeview
for contact in contacts:
	my_tree.insert('', END, values=contact)


root.mainloop()
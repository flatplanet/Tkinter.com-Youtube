from tkinter import *
import customtkinter
import numpy
import pandas as pd
from tkinter import ttk, filedialog, messagebox

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Excel Treeview')
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry("850x400")

def open_excel():
	#open a file
	my_file = filedialog.askopenfilename(title="Open File",
		filetype=(("Excel Files", ".xlsx"),("All Files", "*.*")))

	# grab the file
	try:
		# Create a dataframe
		df = pd.read_excel(my_file)
		
	except Exception as e:
		messagebox.showerror("Woah!", f'There was a problem! {e}')

	# Clear the treeview
	my_tree.delete(*my_tree.get_children())

	# Get the Headers
	my_tree['column'] = list(df.columns)
	my_tree['show'] = 'headings'

	# Show the headers
	for col in my_tree['column']:
		my_tree.heading(col, text=col)

	# Show Data
	df_rows = df.to_numpy().tolist()
	for row in df_rows:
		my_tree.insert("", "end", values=row)



# Treeview
my_tree = ttk.Treeview(root)
my_tree.pack(pady=20)

# hack the column height
my_tree.heading('#0', text="\n")

# Set tree style
style = ttk.Style()
style.theme_use("default")

# change style colors
style.configure("Treeview",
	background="#707070",
	foreground="black",
	rowheight=25,
	fieldbackground="#707070")

# Change color of headers
style.configure("Treeview.Heading", 
	background="#535353",
	foreground="black")

# change color of selected row
style.map('Treeview', background=[('selected', "#535353")])


# Button
my_button = customtkinter.CTkButton(root, text="Open Excel File", command=open_excel)
my_button.pack(pady=20)


root.mainloop()
from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.title("Check Number Of Files...")
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry('500x350')

def checker():
	# Create counters
	file_count = 0
	dir_count = 0

	# Choose Directory
	input_path = filedialog.askdirectory()

	# Loop and count files
	for root, dirs, files in os.walk(input_path):
		# Count files
		for file in files:
			file_count += 1

		# Count Dirs
		for dir1 in dirs:
			dir_count +=1

		# Update our Label
		my_label.config(text=f'Number Of Files: {file_count}\nNumber of Dirs: {dir_count}')
		




my_label = Label(root, text="Number of Files: ", font=("Helvetica", 28))
my_label.pack(pady=50)

my_button = Button(root, text='Check Number Of Files', command=checker)
my_button.pack()



root.mainloop()

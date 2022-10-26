from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spell Checker")
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry('500x500')

def spellerize():
	# Grab text from box
	get_text = my_text.get(1.0, END)
	# Delete TextBox Text
	my_text.delete(1.0, END)

	# Convert text to blob
	blobby = TextBlob(get_text)
	# fix spelling errors
	my_text.insert(1.0, blobby.correct())


# Build GUI
my_text = Text(root, width=50)
my_text.pack(pady=20)

my_button = Button(root, text="Fix Spelling Errors", command=spellerize)
my_button.pack(pady=20)


root.mainloop()
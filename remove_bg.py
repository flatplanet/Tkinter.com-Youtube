from tkinter import *
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Remove Image Background")
root.geometry('500x700')

# Functions
def open_thing():
	global input_path, my_img
	# open image path
	input_path = filedialog.askopenfilename(title="Open Image",
		filetype=(("PNG Files", ".png"), ("All Files", "*.*")))
	if input_path:
		my_img = ImageTk.PhotoImage(Image.open(input_path))
		pic_label.config(image=my_img, bg="black")

def remove_thing():
	# get file path to save file
	output_path = filedialog.asksaveasfilename(title="Save As",
		filetype=(("PNG Files", '.png'), ("All Files", "*.*")))

	# get file name
	input = Image.open(input_path)
	# remove bg
	output = remove(input)
	# Save the file
	output.save(output_path, 'png')

	# Put new image on the screen
	global my_img
	my_img = ImageTk.PhotoImage(Image.open(output_path))

	# Update label
	pic_label.config(image=my_img)



# Gui
pic_label = Label(root, text='')
pic_label.pack(pady=20)

open_button = Button(root, text="Open Image", command=open_thing)
open_button.pack(pady=20)

remove_button = Button(root, text="Remove Background", command=remove_thing)
remove_button.pack(pady=10)

root.mainloop()
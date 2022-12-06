from tkinter import *
from fpdf import FPDF
from PIL import Image, ImageTk
from tkinter import filedialog


root = Tk()
root.geometry('600x600')

root.title("Save Image As PDF")
root.iconbitmap('codemy.ico')

def opener():
	global get_image, image_path

	# Open File Dialog Box
	input_path = filedialog.askopenfilename(title="Open Image",
		filetype=(("PNG", ".png"), ("All Files", "*.*")))

	# Set file path global to use it later
	image_path = input_path

	if input_path:
		if input_path.endswith(".png"):
			# Get Image
			get_image = ImageTk.PhotoImage(Image.open(input_path))
			# Add Image To Label
			my_label.config(image=get_image)

		else:
			# Add PNG to end of path
			input_path = f'{input_path}.png'
			# Get Image
			get_image = ImageTk.PhotoImage(Image.open(input_path))
			# Add Image To Label
			my_label.config(image=get_image)


def saver():
	# Open file dialog to save pdf
	input_path = filedialog.asksaveasfilename(title="Save PDF",
		filetype=(("PDF", ".pdf"), ("All Files", "*.*")))

	if input_path:
		if input_path.endswith(".pdf"):
			# Create fpdf instance
			pdf = FPDF()
			# Create a pdf page
			pdf.add_page()
			# Add image to page
			pdf.image(image_path, x=50, y=50, w=50, h=50)
			# Save pdf
			pdf.output(input_path, "F")

			# Update label
			my_label.config(image='', text="DONE!")

		else:
			# add pdf file extension
			input_path = f'{input_path}.pdf'
			# Create fpdf instance
			pdf = FPDF()
			# Create a pdf page
			pdf.add_page()
			# Add image to page
			pdf.image(image_path, x=50, y=50, w=50, h=50)
			# Save pdf
			pdf.output(input_path, "F")

			# Update label
			my_label.config(image='', text="DONE!")



my_label = Label(root, text="Open Image", font=("Helvetica, 28"))
my_label.pack(pady=50)

open_button = Button(root, text="Open Image", command=opener)
open_button.pack(pady=10)

save_button = Button(root, text="Save To PDF", command=saver)
save_button.pack()


root.mainloop()
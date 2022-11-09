from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

root = Tk()
root.title("QR Code Generator")
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry('500x550')

def create_code():
	#File Dialog
	input_path = filedialog.asksaveasfilename(title="Save Image",
		filetyp=(("PNG File", ".png"), ("All Files", "*.*")))

	if input_path:
		if input_path.endswith(".png"):
			# Create QR Code from entry box
			get_code = pyqrcode.create(my_entry.get())
			# Save as PNG File
			get_code.png(input_path, scale=5)

		else:
			# Add that .png to the end of the file name
			input_path = f'{input_path}.png'
			# Create QR Code from entry box
			get_code = pyqrcode.create(my_entry.get())
			# Save as PNG File
			get_code.png(input_path, scale=5)

		# Put QR code on screen
		global get_image
		get_image = ImageTk.PhotoImage(Image.open(input_path))
		# Add image to label
		my_label.config(image=get_image)
		
		# Delete entry box
		my_entry.delete(0, END)
		# Flash up a finished message
		my_entry.insert(0, "Finished!")


def clear_all():
	my_entry.delete(0, END)
	my_label.config(image='')

# Decode QR Code
def decode_it():
	# Open a qr code image
	#File Dialog
	input_path = filedialog.askopenfilename(title="Open Image",
		filetyp=(("PNG File", ".png"), ("All Files", "*.*")))

	if input_path:
		# Put QR code on screen
		global get_image
		get_image = ImageTk.PhotoImage(Image.open(input_path))
		# Add image to label
		my_label.config(image=get_image)
		
		# Decode QR Code
		decode_QR = decode(Image.open(input_path))
		#print(decode_QR)
		result_label.config(text=f"QR Decoded: {decode_QR[0].data.decode('ascii')}")


		# Delete entry box
		my_entry.delete(0, END)
		# Flash up a finished message
		my_entry.insert(0, "Finished!")

# Create GUI
my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Create QR Code", command=create_code)
my_button.pack(pady=20)

my_button2 = Button(root, text="Clear", command=clear_all)
my_button2.pack()

my_label = Label(root, text='')
my_label.pack(pady=20)

result_label = Label(root, text='')
result_label.pack(pady=20)

result_button = Button(root, text="Decode QR Code", command=decode_it)
result_button.pack(pady=20)

root.mainloop()
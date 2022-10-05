from tkinter import *
import PyPDF2
from tkinter import filedialog, messagebox

root = Tk()
root.title('Tkinter.com - PDF Text Extractor')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("550x650")

# Open PDF File Function
def open_pdf():
	# get file name
	my_file = filedialog.askopenfilename(title="Open File",
		filetype=(("PDF Files", ".pdf"), ("All Files", "*.*")))
	try:
		# Open File
		pdf_file = PyPDF2.PdfFileReader(my_file)
		# Get the number of pages
		number_of_pages = len(pdf_file.pages)
		# Update Our Pages Label
		pages_label.config(text=f'Showing {my_entry.get()} of {number_of_pages-1} pages...')

		# Select page to read
		page = pdf_file.getPage(int(my_entry.get()))

		# Get the content from the page
		content = page.extractText()

		# Clear the text box
		my_text.delete(1.0, END)

		# Output pdf to text
		my_text.insert(1.0, content)

	except Exception as e:
		messagebox.showerror("Whoah!", f'There was a problem! {e}')

# Text Box
my_text = Text(root, width=60, height=25)
my_text.pack(pady=20)

# LabelFrame and Entry Box
my_label_frame = LabelFrame(root, text="Select Page To Open")
my_label_frame.pack(pady=10)

my_label = Label(my_label_frame, text="Page Number: ")
my_label.grid(column=0, row=0, pady=10, padx=10)

my_entry = Entry(my_label_frame)
my_entry.grid(column=1, row=0, padx=10, pady=10)

# Open Button
my_button = Button(root, text="Open PDF", command=open_pdf)
my_button.pack(pady=20)

# Page Number Label
pages_label = Label(root, text="")
pages_label.pack(pady=20)

root.mainloop()
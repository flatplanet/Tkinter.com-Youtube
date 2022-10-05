from tkinter import *
import PyPDF2
from tkinter import filedialog, messagebox

root = Tk()
root.title('Tkinter.com - PDF Text Extractor')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("550x650")

def open_pdf():
	#open a file
	my_file = filedialog.askopenfilename(title="Open File",
		filetype=(("PDF Files", ".pdf"),("All Files", "*.*")))

	try:
		pdf_file= PyPDF2.PdfFileReader(my_file)
		#Select a Page to read
		page = pdf_file.getPage(int(my_entry.get()))
		#Get the content of the Page
		content=page.extractText()

		# get number of pages
		number_of_pages = len(pdf_file.pages)
		# Update label
		pages_label.config(text=f'Showing {my_entry.get()} of {number_of_pages-1} pages...')

		# Clear text
		my_text.delete(1.0, END)
		#Add the content to TextBox
		my_text.insert(1.0,content)
	except Exception as e:
		messagebox.showerror("Woah!", f'There was a problem! {e}')

my_text = Text(root, width=60, height=25)
my_text.pack(pady=20)

my_label_frame = LabelFrame(root, text="Select Page To Open")
my_label_frame.pack(pady=10)

my_label = Label(my_label_frame, text="Page Number: ")
my_label.grid(column=0, row=0, pady=10, padx=10)

my_entry = Entry(my_label_frame)
my_entry.grid(column=1, row=0, pady=10, padx=10)

my_button = Button(root, text="Open PDF", command=open_pdf)
my_button.pack(pady=20)

pages_label = Label(root, text="")
pages_label.pack(pady=20)


root.mainloop()
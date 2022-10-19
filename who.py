from tkinter import *
import whois

root = Tk()
root.title("Domain Name Lookup")
root.geometry('500x550')

# Lookup Function
def lookup():
	# Delete Text in box
	my_text.delete(1.0, END)

	# Get Domain Info
	domain = my_entry.get()
	domain_info = whois.whois(domain)

	# Loop the output
	for key, value in domain_info.items():
		# Output to text box
		my_text.insert(1.0, f'{key} : {value}' + '\n\n')

# GUI
my_frame = LabelFrame(root, text="Lookup Domain Name")
my_frame.pack(pady=20)

my_entry = Entry(my_frame, font=("Helvetica", 18))
my_entry.grid(row=0, column=0, pady=10, padx=10)

my_button = Button(my_frame, text="Lookup Domain", command=lookup)
my_button.grid(row=0, column=1, padx=10)

my_text = Text(root, width=50)
my_text.pack()


root.mainloop()
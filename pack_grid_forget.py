from tkinter import *

root = Tk()
root.title("Pack/Grid Forget and Destroy - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('500x350')

# Pack/Grid Forget and Destroy



def hide():
	my_frame.pack_forget()

def show():
	my_label.grid(row=0, column=0, columnspan=3, pady=20)

def destroy():
	my_label.destroy()


# Create a quick frame
my_frame = Frame(root)
my_frame.pack(pady=50)

# Create a label
my_label = Label(my_frame, text="Hello World", font=("Helvetica", 24))
my_label.grid(row=0, column=0, columnspan=3, pady=20)

# Grid Stuff
my_button3 = Button(my_frame, text="Hide", command=hide)
my_button4 = Button(my_frame, text="Show", command=show)
my_button5 = Button(my_frame, text="Destroy Forever", command=destroy)



my_button3.grid(row=1, column=0)
my_button4.grid(row=1, column=1, padx=20)
my_button5.grid(row=1, column=2)


my_label2 = Label(root, text="My Name Is John Elder", font=("Helvetica", 24))
my_label2.pack(pady=20)

root.mainloop()


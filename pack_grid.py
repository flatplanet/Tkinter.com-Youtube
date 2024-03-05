from tkinter import *

root = Tk()
root.title("Pack vs. Grid - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('500x350')

# Pack some buttons
my_button1 = Button(root, text="Button")
my_button2 = Button(root, text="Button")

my_button1.pack(pady=(20,0))
my_button2.pack(pady=0, fill=X, padx=20)

# Create a quick frame
my_frame = Frame(root)
my_frame.pack(pady=50)

# Grid Stuff
my_button3 = Button(my_frame, text="Button")
my_button4 = Button(my_frame, text="Button")
my_button5 = Button(my_frame, text="Button")

my_button6 = Button(my_frame, text="Button")


my_button3.grid(row=0, column=0)
my_button4.grid(row=0, column=1, padx=20)
my_button5.grid(row=0, column=2)
my_button6.grid(row=1, column=0, pady=20, columnspan=3, sticky='ew')



root.mainloop()


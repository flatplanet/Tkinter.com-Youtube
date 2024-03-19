from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images - Intro To Tkinter")
root.iconbitmap('images/tkinter.ico')
root.geometry('600x400')

# Create our image
aspen = Image.open("images/aspen.png").resize((250,188))
aspen = ImageTk.PhotoImage(aspen)

# Create a label
my_label = Label(root, image=aspen, bd=2, relief="groove") #raised, ridge, sunken, groove, flat
my_label.pack(pady=20)

# Create a button Image
login = Image.open("images/login.png").resize((75,30))
login = ImageTk.PhotoImage(login)

# Create a button
my_button = Button(root, image=login, bd=0)
my_button.pack(pady=20)





root.mainloop()


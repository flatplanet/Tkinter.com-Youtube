from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Toast Message!")
root.iconbitmap('images/codemy.ico')
root.iconbitmap(default='images/codemy.ico')
root.geometry('300x200')


def clicker():
	toast.show_toast()

toast = ToastNotification(title="My Toast Title",
	message="This is a Toast Message!! WOOHOO!!",
	duration=3000,
	alert=True,
	position=(-1915, 300, 'sw'),
	)

my_button = tb.Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=40)


root.mainloop()
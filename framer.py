from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Frames and Labels!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

def thing():
	pass

my_frame = Frame(root)#, bootstyle="dark")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, text="CLICK ME!", bootstyle="dark", command=thing)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Hello There!", font=("Helvetica", 18), bootstyle="inverse light")
my_label.pack(pady=20)

root.mainloop()
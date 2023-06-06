from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Scrolled Frame!")
root.iconbitmap('images/codemy.ico')
root.iconbitmap(default='images/codemy.ico')
root.geometry('700x350')


# Lets create a scrolled frame
my_frame = ScrolledFrame(root, autohide=False, bootstyle="light")
my_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

# Create some buttons
for x in range(21):
	tb.Button(my_frame, bootstyle="info", text=f'Click Me! {x}').pack(pady=10)




root.mainloop()
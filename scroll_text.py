from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Scrolled Text Widget?!")
root.iconbitmap('images/codemy.ico')
root.iconbitmap(default='images/codemy.ico')
root.geometry('700x350')

# Text Widget
my_text = ScrolledText(root, height=20, width=110, wrap=WORD, autohide=False, bootstyle="danger", hbar=True)
my_text.pack(pady=15)



root.mainloop()
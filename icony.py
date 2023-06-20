from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Icons!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Icons: warning, icon, error, question, info
img = PhotoImage(data=Icon.info)

# Label 
my_label = tb.Label(image=img)
my_label.pack(pady=40)


root.mainloop()
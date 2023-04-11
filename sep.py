from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Separator And Sizegrip")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')


label1 = tb.Label(root, text="Label 1", bootstyle="light")
label1.pack(pady=40)


# Separator
my_sep = tb.Separator(root, bootstyle="info", orient="horizontal")
my_sep.pack(fill="x", padx=100)

label2 = tb.Label(root, text="Label 2", bootstyle="light")
label2.pack(pady=40)

# Sizegrip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(anchor="se", fill="both", expand=True)




root.mainloop()
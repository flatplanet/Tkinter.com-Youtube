from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Style
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))

my_button = tb.Button(text="Hello World!", 
	bootstyle="success", 
	style="success.Outline.TButton",
	width=20)

my_button.pack(pady=40)




root.mainloop()
from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Slider/Scale")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')


def scaler(e):
	my_label.config(text=f'{int(my_scale.get())}%')




# Create a Scale/Slider
my_scale = tb.Scale(root, bootstyle="warning",
	length=400,
	orient="horizontal",
	from_=0,
	to=100,
	command=scaler,
	state="normal")
my_scale.pack(pady=50)

# Create a label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack()


root.mainloop()
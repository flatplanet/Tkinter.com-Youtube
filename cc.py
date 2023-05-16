from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Color Chooser")
root.iconbitmap('images/codemy.ico')
root.iconbitmap(default='images/codemy.ico')
root.geometry('700x350')

def cc():
	# Create Color Chooser
	my_color = ColorChooserDialog()
	# Show Color Chooser
	my_color.show()
	# Return Color Chooser Info
	colors = my_color.result
	# Output to the label  (.hex .hsl .rgb)
	my_label.config(text=colors.hex)
	# Change the bg color of our app to chosen color
	root.configure(background=colors.hex)



my_button = tb.Button(root, text="Click Me!", bootstyle="danger", command=cc)
my_button.pack(pady=40)

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)




root.mainloop()
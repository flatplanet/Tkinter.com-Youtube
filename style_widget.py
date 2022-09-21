from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tkinter.com - Style Individual Widgets')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("500x350")

# Define a Style Widget
style = ttk.Style()
style.theme_use("default")

# Widget Style
style.configure('elder.TButton', 
	foreground="white",
	background="#003066",
	font=("Helvetica", 24),
	padding=[10,10,10,10])

style.map('elder.TButton', background=[('active', '#004ea5')])

'''
Widget Style Names
Button: TButton
Checkbutton: TCheckbutton
Combobox: TCombobox
Entry: TEntry
Frame: TFrame
Label: TLabel
LabelFrame: TLabelFrame
Menubutton: TMenubutton
Notebook: TNotebook
PanedWindow: TPanedwindow
Progressbar:  Horizontal.TProgressbar or Vertical.TProgressbar
Radiobutton: TRadiobutton
Scale: Horizontal.TScale or Vertical.TScale
Scrollbar: Horizontal.TScrollbar or Vertical.TScrollbar
Separator: TSeparator
Sizegrip: TSizegrip
Treeview: Treeview
'''


# Create some Buttons

my_button1 = ttk.Button(root, text="Login", style="elder.TButton")
my_button1.pack(pady=40)

my_button2 = ttk.Button(root, text="Exit")
my_button2.pack(pady=20)


root.mainloop()
from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Notebook Tabs!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x400')

my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

my_label = Label(tab1, text="My Awesome Label!", font=("Helvetica", 18))
my_label.pack(pady=20)

my_text = Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

my_button = tb.Button(tab1, text="Click Me!", bootstyle="danger outline")
my_button.pack(pady=20)

my_label2 = Label(tab2, text="This Is Tab Two!", font=("Helvetica", 18))
my_label2.pack(pady=20)

# Add our frames to the notebook
my_notebook.add(tab1, text="Tab One")
my_notebook.add(tab2, text="Tab Two")




root.mainloop()

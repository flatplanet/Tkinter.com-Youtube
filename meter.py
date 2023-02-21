from tkinter import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Meter!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x650')


def up():
    my_meter.step(10)

def down():
    my_meter.step(-10)


global counter
counter=20

def clicker():
    global counter
    if counter <= 100:
        my_meter.configure(amountused=counter)
        counter += 5
        my_button.configure(text=f'Click Me {my_meter.amountusedvar.get()}')

my_meter = tb.Meter(root, bootstyle="danger", 
    subtext="Tkinter Learned",
    interactive=True,
    textright="%",
    #textleft="$"
    metertype="full", # Can be semi
    stripethickness=10,
    metersize=200,
    padding=50,
    amountused=0,
    amounttotal=100,
    subtextstyle="light"
    )
my_meter.pack(pady=50)

my_button = tb.Button(root, text="Click Me 5", command=clicker)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Step Up", command=up)
my_button2.pack(pady=20)

my_button3 = tb.Button(root, text="Step Down", command=down)
my_button3.pack(pady=20)




root.mainloop()

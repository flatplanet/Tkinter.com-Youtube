from tkinter import *
import ttkbootstrap as tb
import time


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Progress Bars")
root.iconbitmap('images/codemy.ico')
root.geometry('500x250')

# Start
def start():
    my_progress.start(10)

# Stop
def stop():
    my_progress.stop()

# Auto
def auto():
    for x in range(5):
        my_progress['value'] += 20
        my_label.config(text=my_progress['value'])
        # Update one at a time not all at once
        root.update_idletasks()
        # Increment 1 second time
        time.sleep(1)


# Increment 20
def increment():
    #my_progress.step(20)
    my_progress['value'] += 20
    # Get current value
    my_label.config(text=my_progress['value'])

# Progress Bar
my_progress = tb.Progressbar(root, bootstyle='danger striped', 
    maximum=100, 
    mode="determinate",
    length=300, 
    value=0)

my_progress.pack(pady=40)

# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Buttons
my_button = tb.Button(my_frame, text="Increment 20", bootstyle="info", command=increment)
my_button.grid(column=0, row=0, padx=10)

my_button1 = tb.Button(my_frame, text="Start", bootstyle="info", command=start)
my_button1.grid(column=1, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="Stop", bootstyle="info", command=stop)
my_button2.grid(column=2, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="Auto", bootstyle="info", command=auto)
my_button3.grid(column=3, row=0, padx=10)


# Create a label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()

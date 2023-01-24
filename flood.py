from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Floodgauge")
root.iconbitmap('images/codemy.ico')
root.geometry('500x550')


def starter():
	# Start the guage
	my_gauge.start()
	while my_gauge.variable.get() < 80:
		my_label.config(text=f"Position: {my_gauge.variable.get()}")

def stopper():
	my_gauge.stop()

def incrementer():
	my_gauge.step(10)
	my_label.config(text=f"Position: {my_gauge.variable.get()}")



my_gauge = tb.Floodgauge(root, bootstyle="success",
	font=("Helvetica", 18),
	mask="Pos: {}%",
	maximum=80,
	orient="horizontal",
	value=0,
	mode="determinate"
	)
my_gauge.pack(pady=50, fill=X, padx=20)


start_button = tb.Button(root, text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)

stop_button = tb.Button(root, text="Stop", bootstyle="danger outline", command=stopper)
stop_button.pack(pady=20)

inc_button = tb.Button(root, text="Increment", bootstyle="danger outline", command=incrementer)
inc_button.pack(pady=20)

my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)



root.mainloop()
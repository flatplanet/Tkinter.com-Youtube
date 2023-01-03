import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the display
display = tk.Entry(window, width=35, bg="white")
display.grid(row=0, column=0, columnspan=5)

# Create the buttons
button_list = [    '7', '8', '9', '+', '-',    '4', '5', '6', '*', '/',    '1', '2', '3', '<-', 'C',    '0', '.', '=', '+/-', 'sqrt']

# Create the button functions
def button_click(number):
    # Insert the number into the display
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    # Clear the display
    display.delete(0, tk.END)

def button_equal():
    # Evaluate the expression and display the result
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def button_sign():
    # Change the sign of the number in the display
    try:
        if display.get()[0] == '-':
            display.delete(0)
        else:
            display.insert(0, '-')
    except:
        pass

def button_square_root():
    # Find the square root of the number in the display
    try:
        result = eval(display.get())**0.5
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the buttons and place them in the grid
row = 1
col = 0
for button in button_list:
    def cmd(temp=button):
        button_click(temp)
    tk.Button(window, text=button, width=5, command=cmd).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Add the special buttons
tk.Button(window, text="<-", width=5, command=lambda:display.delete(len(display.get())-1)).grid(row=row, column=col)
col += 1
tk.Button(window, text="C", width=5, command=button_clear).grid(row=row, column=col)
col += 1
tk.Button(window, text="=", width=5, command=button_equal).grid(row=row, column=col)
col += 1
tk.Button(window, text="+/-", width=5, command=button_sign).grid(row=row, column=col)
col += 1

window.mainloop()

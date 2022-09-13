from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk()
root.title('Tkinter.com - Styles and Themes')
root.iconbitmap('c:/tkinter.com/images/codemy.ico')
root.geometry("500x350")


# Define style
style = ttk.Style(root)
style.theme_use("default")

# See included styles
print(ttk.Style().theme_names())
our_themes = ttk.Style().theme_names()
our_themes2 = root.get_themes()

# Change style
def changer(theme):
	# Change style
	style.theme_use(theme)
	my_label.config(text=f'Login - {theme} Theme')

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

theme_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Themes", menu=theme_menu)

# Sub menu
for t in our_themes2:
	theme_menu.add_command(label=t, command=lambda t=t: changer(t))


# Create Our Widgets
# Header Label
my_label = ttk.Label(root, text="Login", font=("Helvetica", 18))
my_label.pack(pady=20)

# Login Frame
my_frame = ttk.Frame(root)
my_frame.pack(pady=20)

# Username and Password Entry Boxes and Labels
un_label = ttk.Label(my_frame, text="User Name: ")
un_label.grid(row=0, column=0, padx=10, pady=(20,5))

un_entry = ttk.Entry(my_frame)
un_entry.grid(row=0, column=1, padx=10, pady=(20,5))

pw_label = ttk.Label(my_frame, text="Password:")
pw_label.grid(row=1, column=0, padx=10, pady=(0,20))

pw_entry = ttk.Entry(my_frame, show="*")
pw_entry.grid(row=1, column=1, padx=20, pady=(0,20))


# Login Button
my_button = ttk.Button(root, text="Login")
my_button.pack(pady=0)


# Radio Buttons
radio_frame = Frame(root)
radio_frame.pack(pady=20)

var = IntVar()
my_radio1 = ttk.Radiobutton(radio_frame, text="Remember Me", variable=var, value=1,)
my_radio1.grid(row=0, column=0, padx=20)

my_radio1 = ttk.Radiobutton(radio_frame, text="Don't Remember Me", variable=var, value=2,)
my_radio1.grid(row=0, column=1)




root.mainloop()
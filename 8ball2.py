from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Tkinter.com - Magic 8-Ball!')
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry("500x500")

# Define Our Images
meter = ImageTk.PhotoImage(Image.open("images/8ball.png"))
#add_list_image = ImageTk.PhotoImage(Image.open("images/add-list.png").resize((20,20), Image.ANTIALIAS))

meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=35)

def shake():
	answers = {"Yes definitely":"green",
		"You may rely on it":"green",
		"As I see it, yes":"green",
		"Most likely":"green",
		"Outlook good":"green",
		"Yes":"green",
		"Signs point to yes":"green",

		"Reply hazy, try again":"yellow",
		"Ask again later":"yellow",
		"Better not tell you now":"yellow",
		"Cannot predict now":"yellow",
		"Concentrate and ask again":"yellow",

		"Don't count on it":"red",
		"My reply is no":"red",
		"My sources say no":"red",
		"Outlook not so good":"red",
		"Very doubtful":"red"}

	l = list(answers.items())
	
	random.shuffle(l)


	results.config(text=l[0][0], fg=l[0][1])	
	
#Results
results = Label(root, text="", font=("Helvetica", 28), bg="#1a1a1a")
results.pack(pady=20)

# Create Our Buttons
button_1 = customtkinter.CTkButton(master=root, text="Shake 8-Ball", width=190, height=40, compound="top", command=shake)
button_1.pack(pady=30)




root.mainloop()
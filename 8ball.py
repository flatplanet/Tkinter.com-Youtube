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

# Shake The 8-Ball Function
def shake():
	answers = {
		"It is certain": "green",
		"It is decidedly so": "green",
		"Without a doubt":"green",
		"Yes definitely":"green",
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

		"Don't count on it!":"red",
		"My reply is no!":"red",
		"My sources say no!":"red",
		"Outlook not so good!":"red",
		"Very doubtful!":"red"}
	# Convert dictionary to list
	answer_list = list(answers.items())
	# shuffle the list
	random.shuffle(answer_list)
	#print(answer_list)
	# Output to the screen
	results.config(text=answer_list[0][0], fg=answer_list[0][1])



# Define Our Images
ball = ImageTk.PhotoImage(Image.open("images/8ball.png"))
ball_img = Label(root, image=ball, bd=0)
ball_img.pack(pady=35)

# Set Results
results = Label(root, text="", font=("Helvetica", 28), bg="#1a1a1a")
results.pack(pady=20)

# Define Our Button
my_button = customtkinter.CTkButton(master=root, text="Shake 8-Ball", width=190, height=40, compound="top", command=shake)
my_button.pack(pady=30)

root.mainloop()
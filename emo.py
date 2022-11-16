from tkinter import *
import emoji

root = Tk()
root.title("Emoji's")
root.iconbitmap('c:/tkinter.com/codemy.ico')
root.geometry('500x350')

# Create a Label
my_label = Label(root, text=f'{emoji.emojize(":astonished_face:")} {emoji.emojize(":face_screaming_in_fear:")}', font=("Helvetica", 32), fg="red")
my_label.pack(pady=50)



root.mainloop()
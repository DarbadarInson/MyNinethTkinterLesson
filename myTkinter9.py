from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser

def choose_color():

	# variable to store hexadecimal code of color
	color_code = colorchooser.askcolor(title ="Choose color") 
	print(color_code)

root = Tk()

button = Button(root, text = "Select color",
				command = choose_color)
button.pack()
root.geometry("300x300")
root.configure(bg="dark blue")
root.mainloop()

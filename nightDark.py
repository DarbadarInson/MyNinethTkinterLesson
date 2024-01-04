from tkinter import *

window = Tk() 
window.title("Theme Changer") 
window.geometry("480x650") 
window.config(bg="white") 


light = PhotoImage(file="light.png") 
dark = PhotoImage(file="dark.png") 

switch_value = True


def toggle(): 

	global switch_value 
	if switch_value == True: 
		switch.config(image=dark, bg="#26242f", 
					activebackground="#26242f") 
		

		window.config(bg="#26242f") 
		switch_value = False

	else: 
		switch.config(image=light, bg="white", 
					activebackground="white") 
		

		window.config(bg="white") 
		switch_value = True



switch = Button(window, image=light, 
				bd=0, bg="white", 
				activebackground="white", 
				command=toggle) 
switch.pack(padx=50, pady=150) 

window.mainloop() 

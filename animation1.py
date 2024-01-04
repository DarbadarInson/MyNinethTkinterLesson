from tkinter import *

root = Tk()
root.geometry("480x600")
root.configure(bg="dark slate gray")


button = Button(root, bg="blue", fg="gray", text="ANIMATION",
                font=("Bold", 23), activebackground="navy",
                activeforeground="bisque3")

button.place(x=150, y=200)

root.mainloop()
from tkinter import *
from tkinter.ttk import *

ws=Tk()
Progress_Bar=Progressbar(ws,orient=HORIZONTAL,length=250,mode='determinate')

def Slide():
    import time
    Progress_Bar['value']=10
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=20
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=30
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=40
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=50
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=60
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=70
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=80
    ws.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=90
    ws.update_idletasks()
    time.sleep(1)

    Progress_Bar['value']=100

Progress_Bar.pack()
Button(ws,text='Click Me',command=Slide).pack(pady=10)
mainloop()
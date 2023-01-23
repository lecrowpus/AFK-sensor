# import imp
import time
import os
# import startc
from tkinter import *
root=Tk()
root.maxsize(width=700,height=400)
root.minsize(width=700,height=400)
os.startfile('afksensour.py')
def loop():
    global sec,min,hr,clock,i

    sec=sec+1
    if sec==60:
        sec=0
        min+=1
    if min==60:
        min=0
        hr+=1
    i=i+1
    clock.config(text=f"{hr}:{min}:{sec}")


    clock.after(1000,loop)
def close_assistant() :
    f=open("log-time.txt","a")
    f.write(f"\n{hr}:{min}:{sec} Date:{time.strftime('%d:%m:%Y')}")
    f=open("communicate.txt","w")
    f.write('True')
    f.close()
    root.quit()
    pass       

global clock

clock=Label(root,font=100)
clock.pack(side=LEFT,anchor="nw")
sec=0
min=0
hr=0  
i=0
loop()
root.protocol('WM_DELETE_WINDOW',close_assistant) #control the closing of file

Button(root,text='start').pack()


root.mainloop()








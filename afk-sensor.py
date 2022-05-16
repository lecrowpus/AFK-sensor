
from pynput.keyboard import *
import time

def changer(key):
    global c
    
    if key==False:
        return c
    else:
        c+=1
        return c
def timer():
    global c
    c=0
    sec=0
    min=0
    hr=0
    while True:
        sec+=1
        c=changer(key=False)
        if sec==60:
            sec=0
            min+=1
        if min==60:
            min=0
            hr+=1
        if c<1:
            pass
        else :
            loop(key=None)
            break    
        def conector(key):
            changer(key=True)
        print(f"{hr}:{min}:{sec}")
        with Listener(on_press=conector) as l:
            time.sleep(1)
            l.stop()

def afk_f(var):
    global afk
    
    if var==True:
        afk+=1
        return afk   
    
    else:
        afk=0 
        return afk   
def loop(key):
    global afk
    afk=0

    while afk<10:
        def reset(key):
            return afk_f(var=False),False
        with Listener(on_press=reset) as l:
            time.sleep(1)
            l.stop()
        afk=afk_f(var=True)
        print(afk)
    timer()
loop(key=None)


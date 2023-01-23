import sys
from pynput.keyboard import *
import time
global time_,sec,min,hr
sec=0
min=0
hr=0
time_=(f"{hr}:{min}:{sec} Date:{time.strftime('%d:%m:%Y')}")
# checks to close the frpgram
def checker(time):
    f=open("communicate.txt","r")
    q=f.read()
    f.close()
    if q=="True":
        f=open("log-afk-time.txt",'a')
        f.write("\n",time)
        f.close()
        f=open("communicate.txt","w")
        f.write('')
        f.close()
        sys.exit()
    else:
        pass  


def breakloop(key):
    global c
    if key==False:#comes from the third line of thw while loop marked as $
        return c

    else:# changes the c to 1 to break the loop in the else statements 
        c+=1
        return c
def timer():
    global c,time_,hr,min,sec
    c=0# this is a temperiory var 
    #starts the time counts the actual afk(ing) time
    while True:
        time_=(f"{hr}:{min}:{sec} Date:{time.strftime('%d:%m:%Y')}")
        sec+=1
        c=breakloop(key=False) #  $
        if sec==60:
            sec=0
            min+=1
        if min==60:
            min=0
            hr+=1
        if c<1:
            pass
        else :#breaks the loop and starts pretimer
            pretimer(key=None)
            break 

        def conector(key):
            breakloop(key=True)#breaks the timer and starts the pretimer

        print(f"{hr}:{min}:{sec}")

        with Listener(on_press=conector) as l:# if the key is not pressed the timer wont break
            time.sleep(1)
            l.stop()

def afk_f(var):
    global afk
    if var==True:#continues the pretimer 
        afk+=1
        return afk   

    else:#resets the pretimer if the key is pressed in the pretimer
        afk=0 
        return afk 


def pretimer(key):
    global afk
    afk=0
    while afk<10:#pre timer time (the duration of pre timer)
        checker(time=time_)#ckecks if main program wants to close the sensor
        
        def reset(key):#resets the pre timer if the key is pressed in the pretimer
            return afk_f(var=False),False
        
        with Listener(on_press=reset) as l:
            time.sleep(1)
            l.stop()

        afk=afk_f(var=True)#continues the pre timer 

        print(afk)
    
    timer()#runs if the pertime is exeded


pretimer(key=None)



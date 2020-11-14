#!/usr/bin/env python3
from pynput import keyboard
from time import sleep
from threading import Thread
from datetime import datetime


def appendTimeCount():
    global count
    with open("key_log", 'a') as file1: 
        file1.write(datetime.now().strftime('%H:%M') +" "+ str(count) + "\n") 
    count = 0

def on_press(key):
    global count
    count+=1

def on_release(key):
    pass
    
def listeners():
    global count
    count = 0
        
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    
def clocker():
    global count
    count = 0
    
    Thread(target = appendTimeCount).start()
    while True:
        sleep(60) #hour
        if datetime.now().minute == 0:
            Thread(target = appendTimeCount).start()
            if datetime.now().hour == 0:
                with open("key_log", 'a') as file1: 
                    file1.write("\n" + datetime.today().strftime('%Y-%m-%d') + "\n") 
            
    

def main():
    with open("key_log", 'a') as file1: 
        file1.write("\n" + datetime.today().strftime('%Y-%m-%d') + "\n") 
    Thread(target = appendTimeCount).start()
    t1 = Thread(target=clocker) 
    t2 = Thread(target=listeners) 
    t1.start()
    t2.start()
main()

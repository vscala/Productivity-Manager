from tkinter import *
from sys import exit
def popupError(s):
    root = Tk()
    
    root.wm_attributes('-type', 'splash')
    root.title("Notification")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.after(12000, exit)
    popupButton = Button(root, text = s, font = ("Verdana", 12), bg = "gray", command = exit)
    popupButton.pack()
    root.geometry('300x40+' + str(screen_width) + '+0')
    root.mainloop()
    
    
popupError("Characters typed in past hour:" + str(5))

import pyautogui as pg
from os import startfile
import time
import tkinter as tk
from tkinter import ttk
import subprocess

from PIL import Image, ImageTk, UnidentifiedImageError

pg.FAILSAFE = False

x, y = 0, 0
activated = True
run = True

def exitApp():
    #closeApp()
    exit()

def main_mouse_act():
    global activated, run
    #print(event, "ok")
    mouse_x = 1100   #712
    mouse_y = 750    #750
    
    if activated:
        run = True
    else:
        run = False
    if run:
        pg.moveTo(mouse_x, mouse_y)
        pg.leftClick()

        print("ok")
    root.after(300000, main_mouse_act)  #300000


def mouse_act(*event):

    global activated
    if activated:
        mouse_action_button.config(text="De-Activated")
        activated = False
    else:
        mouse_action_button.config(text="Activated")
        activated = True



def open_chrome_incognito():
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito"])

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    #x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    #root.geometry("+%s+%s" % (x , y))
    x =event.x - lastClickX + root.winfo_x()
    root.geometry("+%s+0" % x)

#ui--------------------------------------
root = tk.Tk()
root.title = "Taskbar"
root.attributes('-topmost', True)
root.overrideredirect(1)
root.attributes("-alpha", 0.7)
root.geometry('483x38+442+-37')  #('483x38+658+-37') '324x47+758+-45'             '+x+y'758

widgets_container = tk.Frame(root)
widgets_container.pack(side=tk.LEFT)

#time_container = tk.Frame(root)
#time_container.pack(side=tk.RIGHT)

ultimate_container = tk.Frame(root)
ultimate_container.pack(side=tk.RIGHT)
#root.resizable(0, 0)
#root.attributes('-transparentcolor', root['bg'])

#time Updater
def update_time():
    currentime = time.strftime("%H:%M:%S\n%a %d")
    timelabel.config(text=currentime)
    timelabel.after(1000, update_time)

#ends here

img = Image.open("customtaskbar_images/chromelogo.png")
img = img.resize((32, 32), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img)

chrome_application_button = tk.Button(widgets_container, image=tkimage, command = open_chrome_incognito)
chrome_application_button.grid(row=0, column=0)
chrome_application_button.image = tkimage

mouse_action_button = tk.Button(widgets_container, text = "Activated", width=10, command=mouse_act)
mouse_action_button.grid(row=0, column =1, sticky=tk.N+tk.S)


timelabel = tk.Label(ultimate_container, font=("Courier", 11), height=2, anchor=tk.S)
timelabel.grid(row=0, column=0, sticky=tk.N+tk.E)

pixelVirtual = tk.PhotoImage(width=1, height=1, )
exit_application_button = tk.Button(ultimate_container, image = pixelVirtual, command= exitApp, bg= "#3b5998", width = 2 , height =44)#tk.Button(ultimate_container, image=tkimage, command= exitApp)
exit_application_button.grid(row=0, column=1)
#exit_application_button.image = tkimage

def enteredWindow(event):
    for i in range(45):
        if root.winfo_y() >= 0:
            break
        else:
            root.geometry("+%s+%s" % (root.winfo_x() , int(root.winfo_y())+1))
            root.update()

def leftWindow(event):
    pos_x = pg.position()[0]
    pos_y = pg.position()[1]
    window_x, window_y = list(map(int, root.geometry().split("+")[1:3]))
    #if 658<=pos_x<=1262 and 0<=pos_y<=47:                  #785<=pos_x<=1162 and 0<=pos_y<=47:
    if window_x<=pos_x<=window_x+604 and 0<=pos_y<=47:
        pass
    else:
        for i in range(50):
            if root.winfo_y() <= -35:
                break
            else:
                root.geometry("+%s+%s" % (root.winfo_x() , int(root.winfo_y())-1))
                root.update()

root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.bind('<Enter>', enteredWindow)
root.bind('<Leave>', leftWindow)

update_time()
main_mouse_act()
root.mainloop()
import pyautogui as pg
import time
import tkinter as tk
import keyboard as kb

mouse_x = 1100#712
mouse_y = 750#750

def main_mouse_act(*event):
    print(event, "ok")
    root.after(300000, main_mouse_act)

root = tk.Tk()

main_mouse_act()

while True:
    root.update()
    
    pg.moveTo(x, y)#(1170, y)
    #time.sleep(0.2)
    pg.leftClick()
    #pg.moveTo(x, y)
    #pg.leftClick()

    print("ok")
    time.sleep(300)
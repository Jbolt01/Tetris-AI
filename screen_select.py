import tkinter as tk
import time
import keyboard

root = tk.Tk()
# use transparency level 0.1 to 1.0 (no transparency)
root.attributes('-alpha', 0.2)


def find_BBox():
    while True:
        root.update_idletasks()
        root.update()
        if keyboard.is_pressed('o'):
            top_left_x = root.winfo_rootx()
            top_left_y = root.winfo_rooty()
            height = root.winfo_height()
            width = root.winfo_width()
            bottom_right_x = top_left_x + width
            bottom_right_y = top_left_x + height
            root.destroy()
            break
    return tuple((top_left_x, top_left_y, bottom_right_x, bottom_right_y))

import time
import tkinter as tk

import pyautogui


def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)  # for path  'path/backslash/{}.png'
    time.sleep(4)
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()

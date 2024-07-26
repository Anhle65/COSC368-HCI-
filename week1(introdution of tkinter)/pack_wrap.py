from tkinter import *

from tkinter.ttk import * 

window = Tk()

side_labels = ["bottom1", "bottom2", "top1", "top2", "top3", "top4", "left1", "left2", "right1", "right2"]

for theside in side_labels:

    button = Button(window, text=theside)

    button.pack(side=theside[0:-1])

window.mainloop()
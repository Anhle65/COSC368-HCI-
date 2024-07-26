

from tkinter import *

from tkinter.ttk import * 

window = Tk()

for label_num in range(6):

    button = Button(window, text="Button" + str(label_num))

    button.grid(row=label_num // 2, column=label_num % 3)

    if label_num==1:

        button.grid(columnspan=2, sticky="ew") # compass directions (N, E, S, W)

    elif label_num==3:

        button.grid(rowspan=2, sticky="ns") # compass directions (N, E, S, W)

window.columnconfigure(1, weight=1)

window.rowconfigure(1, weight=1)

window.rowconfigure(2, weight=1)

window.mainloop()


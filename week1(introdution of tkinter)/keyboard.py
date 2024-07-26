from tkinter import *
from tkinter import ttk

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = Tk()
data = StringVar()
label = Label(window, textvariable=data, wraplength=200)
label.grid(row=0, column=0, padx=20, pady=10, sticky='w')
frame = Button(window, border=2)
frame.grid(row=1, columnspan=2, padx=10, pady=10, sticky='we')

def clear_data(data):
    data.set("")

clear = ttk.Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=0, column=1, padx=30, pady=5, sticky='e')
def append(char):
    new_string = data.get() + char
    data.set(new_string)

pad = 0
for i in range(len(board)):
    row = Frame(frame, height=64, width=64)
    row.pack_propagate(0)
    row.grid(row=i,padx= pad, sticky='we')
    pad += 20
    for j in range(len(board[i])):
        button = Button(row, text=board[i][j], height=1, width=1, command=lambda x=board[i][j]: append(x)) 
        button.grid(row=i, column=j, sticky='we')
window.mainloop()
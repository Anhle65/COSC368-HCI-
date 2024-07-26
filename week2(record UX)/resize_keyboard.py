from tkinter import *

from tkinter import ttk 
import random

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = Tk()
data = StringVar()
label = Label(window, textvariable=data)
label.grid(row=0, column=0, padx=350, pady=10)
frame = Button(window, border=2, height=64, width=64)
frame.grid(row=1, columnspan=2, padx=10, pady=10, sticky='we')
frame.pack_propagate(0)

# Text to test on interface
text_test = []

# Add character on the label showing on screen
def check_letter(char):
    global index
    global length
    if char == data.get():
        if index < length-1:
            index += 1
            data.set(target_text[index])
        else:
            data.set("You finish all blocks")
    
index = 0
# Create the interface of keyboard for testing
pad = 0
for i in range(len(board)):
    row = Frame(frame, height=64, width=64, padx= pad, pady=5)
    row.pack_propagate(0)
    row.grid(row=i, sticky='e')
    for j in range(len(board[i])):
        text_test.append(board[i][j])    # Add characters into a list
        square = Frame(row, height=64, width=64)
        square.pack_propagate(0)
        square.grid(row=i,column=j, padx=1)
        button = Button(square, text=board[i][j], command=lambda x=board[i][j]: check_letter(x))
        button.pack(fill=BOTH, expand=1)
    pad += 20

random.shuffle(text_test)
chosen_characters = text_test[:6]
target_text = []
for i in range(1):
    target_text += chosen_characters
    random.shuffle(chosen_characters)
    print(target_text)
length = len(target_text)

import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



data.set(target_text[0])
window.mainloop()
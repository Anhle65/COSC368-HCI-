import time
from tkinter import *
import csv
from tkinter import ttk 
import random

# Set up keyboard
characters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
def randomised_keyboard(characters):
    random.shuffle(characters)
    board = [[c for c in characters[:10]], [c for c in characters[10:19]], [c for c in characters[19:]]]
    return board
board = randomised_keyboard(characters)

# Virtual keyboard
window = Tk()
data = StringVar()
label = Label(window, textvariable=data, padx=300, wraplength=100)
label.grid(row=0, column=0, sticky='n')
frame = Button(window, border=2, height=64, width=64)
frame.grid(row=1, columnspan=2, padx=10, pady=10, sticky='we')
frame.pack_propagate(0)
    
# Text to test on interface
text_test = []
condition = ['static', 'dynamic']
index = 0
random.shuffle(condition)
condition = condition[0]

# Create the interface of keyboard for testing
def keyboard_interface(board):
    pad = 0
    for i in range(len(board)):
        row = Frame(frame, height=64, width=64, padx= pad, pady=5)
        row.pack_propagate(0)
        row.grid(row=i)
        for j in range(len(board[i])):
            text_test.append(board[i][j])    # Add characters into a list
            square = Frame(row, height=64, width=64)
            square.pack_propagate(0)
            square.grid(row=i,column=j, padx=1)
            button = Button(square, text=board[i][j], command=lambda x=board[i][j]: check_letter(x))
            button.pack(fill=BOTH, expand=1)
        pad += 20
keyboard_interface(board)
# Create n-blocks of characters for each experiment
random.shuffle(text_test)
chosen_characters = text_test[:6]
def characters_in_block(chosen_characters):
    random.shuffle(chosen_characters)
    return chosen_characters
length = len(chosen_characters)
target_blocks = 6
testing_characters = characters_in_block(chosen_characters)
current_char = testing_characters[0]
data.set(current_char)
current_block = 1
start = time.time()
# Target character for testing
def check_letter(char):
    global target_blocks
    global current_char
    global index
    global length
    global condition
    global chosen_characters
    global current_block
    global start
    global board
    global testing_characters
    if char == data.get():
        total_time = (time.time() - start) * 1000
        write_record(total_time, current_char)
        if condition == 'dynamic':
            board = randomised_keyboard(characters)
            keyboard_interface(board)
        if index+1 < length:
            index += 1
            current_char = testing_characters[index]
            data.set(testing_characters[index])
        else:
            index = 0
            current_block += 1
            if current_block > target_blocks:
                data.set("You finish all blocks")
            else:
                testing_characters = characters_in_block(chosen_characters)
                current_char = testing_characters[index]
                data.set(current_char)
        start = time.time()
if condition == 'static':
    file = './week2(record UX)/experiment_static_log.txt'
else:
    file = './week2(record UX)/experiment_dynamic_log.txt'
with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'condition', 'target character', 'block-count', 'time taken to click key'])

def write_record(total_time, current_char):
    global condition
    global current_block
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Anh', condition, current_char, current_block, total_time])

window.mainloop()
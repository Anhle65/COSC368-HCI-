import csv
from tkinter import *

from tkinter.ttk import * 

import random

import time

master = Tk()

c = Canvas(master, width=1000, height=400)

c.pack()
distances = [64, 128, 256, 512]
widths = [8, 16, 32]
combination = []
for d in distances:
    for w in widths:
        combination.append((d,w))

rect1 = c.create_rectangle(0, 0, 20, 400, fill="blue")
rect2 = c.create_rectangle(0, 0, 20, 400, fill="green")
global x_cood_rec1, rec1_margins, x_cood_rec2, rec2_margins, thick, space

def random_position():
    global space, thick
    random.shuffle(combination)
    space, thick = combination[-1]
    combination.pop()
    total_span = thick + space
    return thick, space, total_span

def set_rect_position():
    global rect1, rect2, x_cood_rec1, rec1_margins, x_cood_rec2, rec2_margins
    thick, space, total_span = random_position()
    rec1_margins = (1000-total_span)/2
    x_cood_rec1 = rec1_margins + thick

    c.coords(rect1, rec1_margins, 0, x_cood_rec1, 400)

    x_cood_rec2 = x_cood_rec1 + space
    rec2_margins = rec1_margins + space

    c.coords(rect2, rec2_margins, 0, x_cood_rec2, 400)

def swap_rect():
    global rect1, rect2, counter, x_cood_rec1, rec1_margins, x_cood_rec2, rec2_margins
    if counter % 2 == 0:
        c.coords(rect1, rec2_margins, 0, x_cood_rec2, 400)
        c.coords(rect2, rec1_margins, 0, x_cood_rec1, 400)
    else:
        c.coords(rect2, rec2_margins, 0, x_cood_rec2, 400)
        c.coords(rect1, rec1_margins, 0, x_cood_rec1, 400)

start = time.time()
counter = 1
set_rect_position()
def close_screen(event):
    master.quit()

def click_rect2(event):
    global counter, start
    total_time = (time.time() - start) * 1000
    write_record(total_time)
    counter += 1
    swap_rect()
    if counter > 4:
        counter = 1
        if len(combination) > 0:
            set_rect_position()
        else:
            c.delete(rect1, rect2)
            c.create_text(500, 150, text="You finished the experiment. Thank you for your precious time.\n Have a good day =D", fill="black", font=('Helvetica 15 bold'))
            c.create_text(550, 250, text="Click this red button to quit", fill="gray", font=('Helvetica 12 italic'))
            quit = c.create_rectangle(700, 250, 720, 270, fill="red")
            c.tag_bind(quit,"<ButtonPress-1>", close_screen)
    start = time.time()
            
#Write to file
with open("./week3(Fitt's Law)/Fitt_law.txt", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'distance', 'width', 'selection number', 'time'])

def write_record(total_time):
    global space, thick, counter
    with open("./week3(Fitt's Law)/Fitt_law.txt", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Anh', space, thick, counter, total_time])

c.tag_bind(rect2, "<ButtonPress-1>", click_rect2)

master.mainloop()

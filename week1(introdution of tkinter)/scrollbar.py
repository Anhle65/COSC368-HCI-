from tkinter import *
from tkinter import ttk

window = Tk()

data = Text(window, height=10, width=24, wrap='none')

data.insert("1.0","Data to display Data to displayData to displayData to displayData to display\n")
data.grid(row=0, column=0)
vertical = ttk.Scrollbar(window, orient=VERTICAL, command=data.yview)
data.configure(yscrollcommand=vertical.set)
vertical.grid(row=0, column=1, sticky="ns")

horizontal = ttk.Scrollbar(window, orient=HORIZONTAL, command=data.xview)
data.configure(xscrollcommand=horizontal.set)
horizontal.grid(row=1, column=0, sticky="we")

for i in range(30):
    data.insert("end","Data to display\n")
window.mainloop()
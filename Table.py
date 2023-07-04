from tkinter import *
import tkinter as tk
from constants import *
from ClassProduct import *

def Table(window, rows):
  headerTable = ["No. Referencia", "Nombre", "Color", "SKU", "Cant. Kilogramos", "Precio", "Descripción"]
  for x in range(len(rows)):
    for y in range(len(headerTable)):
      frameGrid = tk.Frame(master=window, borderwidth=2)
      frameGrid.grid(row=x, column=y)
      if x == 0:
        labelGrid = tk.Label(master=frameGrid, text=headerTable[y], width=20, height=2, bg=DARK_BLUE, fg="white")
        labelGrid.pack()
      else:
        if y == 0:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getRef(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 1:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getName(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 2:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getColor(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 3:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getSku(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 4:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getQuantityKil(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 5:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getPlace(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
        elif y == 6:
          labelGrid = tk.Label(master=frameGrid, text=rows[x].getDesc(), width=20, height=2, bg="white", fg="black")
          labelGrid.pack()
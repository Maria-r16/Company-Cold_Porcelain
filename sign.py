import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from functools import partial
from constants import *

def Signin(entry_user, entry_password, new):
  
  username = entry_user.get()
  password = entry_password.get()
  
  if (username == USER and password == PASSWORD):
    new.withdraw()
    new_window = tk.Toplevel()
    new_window.geometry(SCREEN_DIMENSIONS)
    new_window.title(TITLE_WINDOWS)
    new_window.configure(bg = BACKGROUND)
    new_window.resizable(False, False)
    
    title = tk.Label(new_window, text = "Control de Inventario", bg= BACKGROUND, fg = DARK_BLUE, font = (FONT, 35, BOLD))
    title.place(x = 550, y = 15)

    # IMAGEN
    labelPicture = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Universidad del Valle\Company-Cold_Porcelain\Imagenes\Loguito.png")
    labelPicture_tk = ImageTk.PhotoImage(labelPicture)
    # Etiqueta de Imagen
    label_Picture = tk.Label(new_window, image=labelPicture_tk, height=100, width=100, bg= BACKGROUND)
    label_Picture.place(x = 20, y = 10)

    #FRAME -COLUMNA #1
    frame = tk.Frame(new_window, width = 350, height= 450, bg= LAVANDER)
    frame.place(x=20, y=120)
    
    # CONTENIDO DE COLUMNA #1
    ref = tk.Label(frame, text= "No. Referencia", bg= LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    ref.place(x = 20, y = 45)
    entry_ref = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_ref.place(width = 160, height = 25, x = 165, y = 50)

    sku= tk.Label(frame, text="SKU", bg= LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    sku.place(x = 55, y = 105)
    entry_sku = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_sku.place(width = 160, height = 25, x = 165, y = 105)

    name = tk.Label(frame, text="Nombre", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    name.place(x = 45, y = 160)
    entry_name = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_name.place(width = 160, height = 25, x = 165, y = 160)

    color = tk.Label(frame, text="Color", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    color.place(x = 47, y = 215)
    entry_color = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_color.place(width = 160, height = 25, x = 165, y = 215)

    quantityKil = tk.Label(frame, text="Cant. Kilogramos", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    quantityKil.place(x = 15, y = 270)
    entry_quantityKil = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_quantityKil.place(width = 160, height = 25, x = 165, y = 270)
  
    #función
    price = tk.Label(frame, text="Precio", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    price.place(x = 45, y = 325)
    entry_price = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_price.place(width = 160, height = 25, x = 165, y = 325)

    desc = tk.Label(frame, text="Descripcion", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    desc.place(x = 25, y = 375)
    entry_desc = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_desc.place(width = 160, height = 25, x = 165, y = 375)

    # FRAME 2 - COLUMNA 2
    # Función Buscar


    new_window.mainloop()

  elif (username != USER and password != PASSWORD):
    messagebox.showerror("Error","Datos ingresados incorrectos")
  elif (password != PASSWORD):
    messagebox.showerror("Error","Contraseña incorrecta")
  elif (username != USER):
    messagebox.showerror("Error","Usuario incorrecto")


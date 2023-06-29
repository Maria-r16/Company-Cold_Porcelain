import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from functools import partial
from constants import *
from Table import Table as tb
from functions import *
from ClassProduct import Product

def Signin(entry_user, entry_password, new):
  
  username = entry_user.get()
  password = entry_password.get()
  p = Product()
  products = [p]
  
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
    labelPicture = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Company-Cold_Porcelain\Imagenes\Loguito.png")
    labelPicture_tk = ImageTk.PhotoImage(labelPicture)
    # Etiqueta de Imagen
    label_Picture = tk.Label(new_window, image=labelPicture_tk, height=100, width=100, bg= BACKGROUND)
    label_Picture.place(x = 20, y = 10)

    #FRAME -COLUMNA #1
    frame = tk.Frame(new_window, width = 350, height= 500, bg= LAVANDER)
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
  
    price = tk.Label(frame, text="Precio", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    price.place(x = 45, y = 325)
    entry_price = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_price.place(width = 160, height = 25, x = 165, y = 325)

    desc = tk.Label(frame, text="Descripcion", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    desc.place(x = 25, y = 375)
    entry_desc = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_desc.place(width = 160, height = 25, x = 165, y = 375)

    # FRAME 2 - COLUMNA 2
    frame_2 = tk.Frame(new_window, width = 1075, height= 750, bg= LAVANDER)
    frame_2.place(x=410, y=120)
    
    # Función Buscar
    frame_search = tk.Frame(frame_2, width = 1050, height= 80, bg= BACKGROUND)
    frame_search.place(x=10, y=10)

    name_search = tk.Label(frame_search, text = "Nombre a buscar", bg = BACKGROUND, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    name_search.place(x=20, y=20 )
    entryName_search = tk.Entry(frame_search, bg = LAVANDER, font = (FONT, 13))
    entryName_search.place(width = 180, height=30, x=170, y=20)

    sku_search = tk.Label(frame_search, text = "SKU", bg = BACKGROUND, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    sku_search.place(x=420, y=20 )
    entrySku_search = tk.Entry(frame_search, bg = LAVANDER, font = (FONT, 13))
    entrySku_search.place(width = 180, height=30, x=470, y=20)
    
    search = entryName_search, entrySku_search

    frame_table = tk.Frame(frame_2, width = 1075, height= 600, bg= BACKGROUND) # se crea el frame que contiene la tabla
    frame_table.place(x=10, y=100)

    button_search = tk.Button(frame_search, text = "Buscar", bg = DARK_BLUE, fg = BACKGROUND, font = (FONT, 14, BOLD), command = partial(searchProducts, search, products, frame_table, tb, frame_2))
    button_search.place(width=180, x = 760, y = 15)

    # Tabla
    tb(frame_table, products) # se crea la tabla
    product = entry_ref, entry_sku, entry_name, entry_color, entry_quantityKil, entry_price, entry_desc

    # Botones
    button_register = tk.Button(new_window, text = 'Registrar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14), command = partial(productRegister, product, products, frame_table, tb, frame_2))
    button_register.place(width=130, x = 20, y = 680)

    button_refresh = tk.Button(new_window, text = 'Actualizar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14))
    button_refresh.place(width=130, x = 215, y = 680)

    button_delete = tk.Button(new_window, text = 'Eliminar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14))
    button_delete.place(width=130, x = 20, y = 750)

    # button_grafics = tk.Button(new_window, text = 'Gráficas', bg= "blue violet", fg = BACKGROUND, font = (FONT, 14))
    # button_grafics.place(width=130, x = 20, y = 820)

    button_out = tk.Button(new_window, text = 'Salir', bg= "red", fg = BACKGROUND, font = (FONT, 14), command = partial(exit, new_window))
    button_out.place(width=130, x = 215, y = 750)

    new_window.mainloop()

  elif (username != USER and password != PASSWORD):
    messagebox.showerror("Error","Datos ingresados incorrectos")
  elif (password != PASSWORD):
    messagebox.showerror("Error","Contraseña incorrecta")
  elif (username != USER):
    messagebox.showerror("Error","Usuario incorrecto")


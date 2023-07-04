import tkinter as tk
from tkinter import ttk
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
  products = []
  
  if (username == USER and password == PASSWORD):
    new.withdraw()
    new_window = tk.Toplevel()
    new_window.geometry(SCREEN_DIMENSIONS)
    new_window.title(TITLE_WINDOWS)
    new_window.configure(bg = BACKGROUND)
    new_window.resizable(False, False)
    isSearch = BooleanVar(new_window, False)
    
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
    
    name = tk.Label(frame, text="Nombre", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    name.place(x = 45, y = 105)
    selec_name = tk.StringVar(frame)
    selec_name.set("Nombre Producto")
    options = ["Foamy Moldeable", "Cold Colores", "Cold Flexible", "Cold Special"]
    menu = tk.OptionMenu(frame, selec_name, *options)
    menu.config(width=20)
    menu.place(width = 160, height = 25, x = 165, y = 105)

    color = tk.Label(frame, text="Color", bg = LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    color.place(x = 47, y = 160)
    selec_color = tk.StringVar(frame)
    selec_color.set("Elegir Color")
    optionsColor = ["Blanco: 101", "Negro: 102", "Cafe claro: 107", "Cafe oscuro: 108", "Amarillo: 109", "Amarillo claro: 110", "Amarillo fluorescente: 111", "Naranja: 112", "Naranja fluorescente: 113", "Rojo: 114", "Rosado: 115", "Fucsia: 116", "Piel clara: 118", "Piel oscura: 119", "Morado: 120", "Azul claro: 126", "Azul oscuro: 128", "Verde claro: 132", "Verde esmeralda: 133", "Verde oscuro: 136","", "Cold Flexible:", "207", "", "Cold Special:", "Tradicional: 203", "Extra blanca: 205"]
    menuColor = tk.OptionMenu(frame, selec_color, *optionsColor)
    menuColor.config(width=20)
    menuColor.place(width = 160, height = 25, x = 165, y = 160)

    sku = tk.Label(frame, text="SKU", bg= LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    sku.place(x = 55, y = 215)
    entry_sku = tk.Entry(frame, bg = BACKGROUND, font = (FONT, 13))
    entry_sku.place(width = 160, height = 25, x = 165, y = 215)

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
    
    # FRAME 3 - Sección Buscar
    frameSearch = tk.Frame(frame_2, width = 1050, height= 600, bg= BACKGROUND)
    frameSearch.place(x=10, y=10)

    name_search = tk.Label(frameSearch, text = "Nombre a buscar", bg = BACKGROUND, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    name_search.place(x=20, y=20 )
    selec_searchName = tk.StringVar(frameSearch)
    selec_searchName.set("Seleccione el nombre")
    optionsSearch = ["Foamy Moldeable", "Cold Colores", "Cold Flexible", "Cold Special"]
    menuSearch = tk.OptionMenu(frameSearch, selec_searchName, *optionsSearch)
    menuSearch.config(width=20, bg=LAVANDER)
    menuSearch.place(width = 180, height=30, x=170, y=20)

    sku_search = tk.Label(frameSearch, text = "SKU", bg = BACKGROUND, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    sku_search.place(x=420, y=20 )
    entrySku_search = tk.Entry(frameSearch, bg = LAVANDER, font = (FONT, 13))
    entrySku_search.place(width = 180, height=30, x=470, y=20)
    
    search = selec_searchName, entrySku_search # recibe las entradas

    frame_table = tk.Frame(frame_2, width = 1050, height= 630, bg= LAVANDER) # se crea el frame que contiene la tabla
    frame_table.place(x=10, y=100)

    # Tabla
    headerTable = ["No. Referencia", "Nombre", "Color", "SKU", "Cant. Kilogramos", "Precio", "Descripción"]
    table = ttk.Treeview(frame_table, columns = headerTable, show = "headings", height = 25)
    table.place(x = 0, y = 10, width = 1050, height = 630)

    for i in headerTable:
      table.heading(i, text = i, bg = DARK_BLUE, fg = BACKGROUND)
      table.column(i, width = 150, anchor = tk.CENTER)

    #scrollbar horizontal
    # scrollbar = ttk.Scrollbar(table, orient=tk.HORIZONTAL, command=table.xview)
    # table.configure(xscroll=scrollbar.set)
    # scrollbar.place(x = 0, y = 605, width = 1050)

    #scrollbar vertical
    scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.place(x = 1030, y = 10, height = 630)
    
    product = entry_ref, selec_name, selec_color, entry_sku, entry_quantityKil, entry_price, entry_desc

    ##on click row
    table.bind('<ButtonRelease-1>', lambda e: getRow(e, table, product, isSearch))

    # Botones
    button_search = tk.Button(frameSearch, text = "Buscar Producto", bg = DARK_BLUE, fg = BACKGROUND, font = (FONT, 14, BOLD), command = partial(searchProducts, search, products, table, isSearch))
    button_search.place(width=180, x = 760, y = 15)
    
    button_register = tk.Button(new_window, text = 'Registrar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14), command = partial(productRegister, product, products, table))
    button_register.place(width=130, x = 20, y = 680)

    button_refresh = tk.Button(new_window, text = 'Actualizar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14), command= partial(updateProduct, product, products, table))
    button_refresh.place(width=130, x = 215, y = 680)

    button_delete = tk.Button(new_window, text = 'Eliminar', bg= DARK_BLUE, fg = BACKGROUND, font = (FONT, 14), command= partial(deleteProduct, product, products, table))
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


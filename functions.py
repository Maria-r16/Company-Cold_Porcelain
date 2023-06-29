import tkinter as tk
from constants import *
from ClassProduct import *

def productRegister(product, arrayProducts, frame, tableConstructor, container):
    # Se crea un objeto de la clase producto y se accede a cada entrada(entry)  
    objProduct = Product(ref=product[0].get(), sku=product[1].get(), name=product[2].get(), color=product[3].get(), quantityKil=product[4].get(), place=product[5].get(), desc=product[6].get())
    arrayProducts.append(objProduct) # Se registran productos
    
    # Actualizando vista
    frame.destroy()
    frame_table = tk.Frame(container, width = 1030, height= 600, bg= BACKGROUND)
    frame_table.place(x=10, y=100)
    tableConstructor(frame_table, arrayProducts)

    # Limpiar campos 
    for i in range(len(product)):
        product[i].delete(0, tk.END)

def searchProducts(product, arrayProducts, frame, tableConstructor, container):
    # Se crea un objeto de la clase producto y se accede a cada entrada(entry)  
    objProduct = Product(sku=product[1].get(), name=product[0].get())
    p = Product()
    
    # Se busca producto
    searchProd = []
    for i in range(len(arrayProducts)):
        if (objProduct.name == arrayProducts[i].name and objProduct.sku == arrayProducts[i].sku):
            foundProduct = Product(ref=arrayProducts[i].ref, sku=arrayProducts[i].sku, name=arrayProducts[i].name, color=arrayProducts[i].color, quantityKil=arrayProducts[i].quantityKil, place=arrayProducts[i].place, desc=arrayProducts[i].desc)
            searchProd.append(foundProduct)

    print(len(arrayProducts), len(searchProd))
    
    # Actualizando vista
    frame.destroy()
    frame_table = tk.Frame(container, width = 1030, height= 600, bg= BACKGROUND)
    frame_table.place(x=10, y=100)
    tableConstructor(frame_table, searchProd)

    # Limpiar campos 
    for i in range(len(product)):
        product[i].delete(0, tk.END)
    
def exit(window):
    window.destroy()
import tkinter as tk
from constants import *
from ClassProduct import *
from tkinter import messagebox

def productRegister(product, arrayProducts, table):
    # Se crea un objeto de la clase producto y se accede a cada entrada(entry)  
    objProduct = Product(ref=product[0].get(), name=product[1].get(), color=product[2].get(), sku=product[3].get(), quantityKil=product[4].get(), place=product[5].get(), desc=product[6].get())
    arrayProducts.append(objProduct) # Se registran productos
    table.insert("", tk.END, values=(objProduct.ref, objProduct.name, objProduct.color, objProduct.sku, objProduct.quantityKil, objProduct.place, objProduct.desc))

    # Limpiar campos 
    for i in range(len(product)):
        if i != 1 and i != 2:
            product[i].delete(0, tk.END)
        elif i == 1:
            product[i].set("Nombre Producto")
        elif i == 2:
            product[i].set("Elegir Color")
    messagebox.showinfo(message="Registrado con éxito", title="Registrar")
            

def searchProducts(search, arrayProducts, table, isSearch):
    isSearch.set(True)
    objProduct = Product(name=search[0].get(), sku=search[1].get())
    for prod in arrayProducts:
        if prod.name == objProduct.name and prod.sku == objProduct.sku:
            # eliminar todas las filas y mostrar el producto encontrado
            table.delete(*table.get_children())
            table.insert("", tk.END, values=(prod.ref, prod.name, prod.color, prod.sku, prod.quantityKil, prod.place, prod.desc))
            # Limpiar campos 
            search[1].delete(0, tk.END)
            search[0].set("Nombre Producto") 
            return
        else:
            messagebox.showerror(title= None, message= "Producto no encontrado")
            return isSearch.set(False)
        
    
def deleteProduct(product, arrayProducts, table, isSearch):
    objProduct = Product(ref=product[0].get(), name=product[1].get(), color=product[2].get(), sku=product[3].get(), quantityKil=product[4].get(), place=product[5].get(), desc=product[6].get())
    
    messageDel = messagebox.askokcancel("Eliminar","¿Desea eliminar producto?")
    if messageDel == True:
        for prod in arrayProducts:
            if prod.name == objProduct.name and prod.sku == objProduct.sku:
                arrayProducts.remove(prod)
                table.delete(*table.get_children())
                for prod in arrayProducts:
                    table.insert("", tk.END, values=(prod.ref, prod.name, prod.color, prod.sku, prod.quantityKil, prod.place, prod.desc))
                messagebox.showinfo(message="Se ha eliminado correctamente", title="Éxito")
                isSearch.set(False)
                return
            else:
                messagebox.showerror(title= None, message="No se logró eliminar producto \n El Nombre y SKU no se puede cambiar")
                return isSearch.set(False)

    # Limpiar campos 
    for i in range(len(product)):
        if i != 1 and i != 2:
            product[i].delete(0, tk.END)
        elif i == 1:
            product[i].set("Nombre Producto")
        elif i == 2:
            product[i].set("Elegir Color")


def updateProduct(product, arrayProducts, table, isSearch):
    objProduct = Product(ref=product[0].get(), name=product[1].get(), color=product[2].get(), sku=product[3].get(), quantityKil=product[4].get(), place=product[5].get(), desc=product[6].get())
    for prod in arrayProducts:
        if prod.name == objProduct.name and prod.sku == objProduct.sku:
            prod.ref = objProduct.ref
            prod.color = objProduct.color
            prod.quantityKil = objProduct.quantityKil
            prod.place = objProduct.place
            prod.desc = objProduct.desc
            table.delete(*table.get_children())
            for prod in arrayProducts:
                table.insert("", tk.END, values=(prod.ref, prod.name, prod.color, prod.sku, prod.quantityKil, prod.place, prod.desc))
            messagebox.showinfo(message="Se actualizo el producto correctamente", title="Éxito")
            isSearch.set(False)
            break
            
        else:
            messagebox.showerror(title= None, message="No se logró actualizar producto \n El Nombre y SKU no se puede cambiar")
            return isSearch.set(False)

    # Limpiar campos 
    for i in range(len(product)):
        if i != 1 and i != 2:
            product[i].delete(0, tk.END)
        elif i == 1:
            product[i].set("Nombre Producto")
        elif i == 2:
            product[i].set("Elegir Color")


def exit(window):
    messagExit = messagebox.askquestion("Salir", "¿Esta seguro que desea salir?")
    if messagExit == "yes":
        window.destroy()


# obtiene los valores de la fila y los envia al formulario
def getRow(event, table, product, isSearch):
      if not isSearch.get():
        return
      
      item = table.item(table.focus())    
      # cargar formulario con los datos de la fila seleccionada
      for i in range(len(product)):
            if i != 1 and i != 2:
                  product[i].delete(0, tk.END)
                  product[i].insert(0, item['values'][i])
            elif i == 1:
                  product[i].set(item['values'][i])
            elif i == 2:
                  product[i].set(item['values'][i])
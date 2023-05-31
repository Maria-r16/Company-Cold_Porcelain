import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from constantes import *
from inicio import Login
from functools import partial

def main():
    ventana = tk.Tk()
    ventana.geometry(DIMENSIONES_DE_PANTALLA)
    ventana.title("Cold Porcelain: Administrativo")
    ventana.configure(bg = "white")
    ventana.resizable(False, False)
    imagen = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Universidad del Valle\Company-Cold_Porcelain\Imagenes\Marca.png")
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget de etiqueta con la imagen
    etiqueta_imagen = tk.Label(ventana, image=imagen_tk, height=300, width=500, bg="white").place(x=250, y=100)

    # Boton de llamado a ventana 2
    boton_admin = tk.Button(ventana, text = "Administrador", bg = "dark blue", fg="white", font = ("calibri", 12), command=partial(Login, ventana))
    boton_admin.place(relx = 0.5, rely = 0.7, width = 200, height=50, anchor = 'c')

    ventana.mainloop()

main()


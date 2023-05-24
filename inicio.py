import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("900x700")
ventana.title("Cold Porcelain: Administrativo")
ventana.configure(bg = "white")

def nuevaVentana():
  ventana.withdraw()
  nueva = tk.Toplevel()
  nueva.geometry("900x700")
  nueva.configure(bg = "white")

imagen = Image.open("/mnt/c/Users/Juanfran/OneDrive/Escritorio/-w-/Company-Cold_Porcelain/Presentación2.png")
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget de etiqueta con la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen_tk, height=300, width=500, bg="white").place(x=200, y=100)

#correo = str(entry_correo.get())
#imagen
#logoImagen = Image.open("/mnt/c/Users/Juanfran/OneDrive/Escritorio/-w-/Company-Cold_Porcelain/Press1.png")
#logoImagen_tk = ImageTk.PhotoImage(logoImagen)
#etiqueta
#etiqueta_logo = tk.Label(nueva, image=logoImagen_tk, height=300, width=500, bg="pink").place(x=200, y=100)
#label_correo = tk.Label(nueva, text = "Ingresar correo electrónico", fg = "dark blue", font = ("calibri", 12))
#label_correo.pack()
#entry_correo = tk.Entry(nueva, bg = "lavender")
#entry_correo.pack()


# Boton de llamado a ventana 2
boton_admin = tk.Button(ventana, text = "Administrador", bg = "dark blue", fg="white", font = ("calibri", 12), command=nuevaVentana)
boton_admin.place(relx = 0.5, rely = 0.7, width = 200, height=50, anchor = 'c')

ventana.mainloop()
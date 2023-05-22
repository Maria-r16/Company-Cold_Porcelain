import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.geometry("900x700")
ventana.title("cold porcelain")
ventana.configure(bg = "white")

imagen = Image.open("/mnt/c/Users/Juanfran/OneDrive/Escritorio/-w-/Company-Cold_Porcelain/porcelain.png")
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget de etiqueta con la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack()

boton_admin = tk.Button(ventana, text = "Administrador", bg = "dark blue", fg="white", font = ("calibri", 12))
boton_admin.place(relx = 0.5, rely = 0.5, width = 130, anchor = 'c')

ventana.mainloop()
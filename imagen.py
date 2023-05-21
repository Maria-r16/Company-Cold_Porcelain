import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()

imagen = Image.open("/mnt/c/Users/Juanfran/OneDrive/Escritorio/-w-/Company-Cold_Porcelain/cold.png")

# Crear el objeto PhotoImage
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget de etiqueta con la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)

# Mostrar la etiqueta en la ventana
etiqueta_imagen.pack()

# Mostrar la ventana
ventana.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
from constants import *
from login import Login
from functools import partial

def main():
    window = tk.Tk()
    window.geometry(SCREEN_DIMENSIONS)
    window.title(TITLE_WINDOWS)
    window.configure(bg = BACKGROUND)
    window.resizable(False, False)
    image = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Company-Cold_Porcelain\Imagenes\Marca.png")
    image_tk = ImageTk.PhotoImage(image)

    # Crear un widget de etiqueta con la imagen
    label_image = tk.Label(window, image=image_tk, height=300, width=500, bg=BACKGROUND)
    label_image.place(x=475, y=150)

    # Boton de llamado a ventana 2
    botton_admin = tk.Button(window, text = "Administrador", bg = DARK_BLUE, fg=BACKGROUND, font = (FONT, 14), command=partial(Login, window))
    botton_admin.place(x = 630, y = 500, width = 200, height=50)

    window.mainloop()

main()


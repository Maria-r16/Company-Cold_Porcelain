import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from sign import Signin
from functools import partial
from constants import *

def Login(window):
  window.withdraw()
  new = tk.Toplevel()
  new.geometry(SCREEN_DIMENSIONS)
  new.title(TITLE_WINDOWS)
  new.configure(bg = BACKGROUND)
  new.resizable(False, False)

  #imagen
  labelImage = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Universidad del Valle\Company-Cold_Porcelain\Imagenes\Logo.png")
  labelImage_tk = ImageTk.PhotoImage(labelImage)

  #etiqueta imagen
  label_Image = tk.Label(new, image=labelImage_tk, height=250, width=200, bg=BACKGROUND)
  label_Image.pack()

  label_user = tk.Label(new, text = "Ingresar Usuario", bg= BACKGROUND, fg = DARK_BLUE, font = (FONT, 14))
  label_user.place(width=320, x=495, y=250)
  entry_user = tk.Entry(new, bg = LAVANDER, font = (FONT, 13))
  entry_user.place(width = 320, height=30, x=590, y=300)

  label_password = tk.Label(new, text = "Ingresar contraseña", bg= BACKGROUND, fg = DARK_BLUE, font = (FONT, 14))
  label_password.place(width=250, x=545, y=380)
  entry_password = tk.Entry(new, bg = LAVANDER, font = (FONT, 13), show="*")
  entry_password.place(width = 320, height=30, x=590, y=430)
  
  #if (entry_password.focus_displayof):
    #if (signin(entry_user, entry_password) == False): 
  label_error = tk.Label(new, text = "Solo puede ingresar el usuario administrativo", bg= BACKGROUND, fg = DARK_BLUE, font = (FONT, 10))
  label_error.place(x=620, y=520)
  
  #Botón
  botton_login = tk.Button(new, text="Ingresar", bg = DARK_BLUE, fg=BACKGROUND, font = (FONT, 14), command=partial(Signin, entry_user, entry_password, new))
  botton_login.place(x = 650, y = 600, width = 200, height=50)
  new.mainloop()

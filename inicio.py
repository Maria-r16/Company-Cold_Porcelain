import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from constantes import *
from functools import partial

def signin(entry_user, entry_password):
  
  username = entry_user.get()
  password = entry_password.get()
  
  if (username == "adminColdPorcelain" and password == "inventario"):
    new_window = tk.Tk()
    new_window.geometry(DIMENSIONES_DE_PANTALLA)
    new_window.title("Cold Porcelain: Administrativo")
    new_window.configure(bg = "white")
    new_window.resizable(False, False)

  elif (username != "adminColdPorcelain" and password != "inventario"):
    messagebox.showerror("Error","Datos ingresados incorrectos")
  elif (password != "inventario"):
    messagebox.showerror("Error","Contraseña incorrecta")
  elif (username != "adminColdPorcelain"):
    messagebox.showerror("Error","Usuario incorrecto")

def Login(ventana):
  ventana.withdraw()
  new = tk.Toplevel()
  new.geometry(DIMENSIONES_DE_PANTALLA)
  ventana.title("Cold Porcelain: Administrativo")
  new.configure(bg = "white")
  new.resizable(False, False)

  #imagen
  logoImagen = Image.open(r"C:\Users\franc\OneDrive\Escritorio\Universidad del Valle\Company-Cold_Porcelain\Imagenes\Logo.png")
  logoImagen_tk = ImageTk.PhotoImage(logoImagen)

  #etiqueta
  etiqueta_logo = tk.Label(new, image=logoImagen_tk, height=250, width=200, bg="white")
  etiqueta_logo.pack()

  label_user = tk.Label(new, text = "Ingresar Usuario", bg= "white", fg = "dark blue", font = ("calibri", 14))
  label_user.place(width=230, x=300, y=250)
  entry_user = tk.Entry(new, bg = "SlateGray3", font = ("calibri", 13))
  entry_user.place(width = 320, height=30, x=345, y=300)

  label_password = tk.Label(new, text = "Ingresar contraseña", bg= "white", fg = "dark blue", font = ("calibri", 14))
  label_password.place(width=250, x=300, y=380)
  entry_password = tk.Entry(new, bg = "SlateGray3", font = ("calibri", 13), show="*")
  entry_password.place(width = 320, height=30, x=345, y=430)
  
  #if (entry_password.focus_displayof):
    #if (signin(entry_user, entry_password) == False): 
  label_error = tk.Label(new, text = "Solo puede ingresar el usuario administrativo", bg= "white", fg = "dark blue", font = ("calibri", 8))
  label_error.place(x=385, y=495)
  
  #Botón
  boton_login = tk.Button(new, text="Ingresar", bg = "dark blue", fg="white", font = ("calibri", 14), command=partial(signin, entry_user, entry_password))
  boton_login.place(relx = 0.5, rely = 0.8, width = 200, height=40, anchor = 'c')
  new.mainloop()
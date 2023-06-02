import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from functools import partial
from constants import *
#from login import *

def Signin(entry_user, entry_password, new):
  
  username = entry_user.get()
  password = entry_password.get()
  
  if (username == USER and password == PASSWORD):
    new.withdraw()
    new_window = tk.Toplevel()
    new_window.geometry(SCREEN_DIMENSIONS)
    new_window.title(TITLE_WINDOWS)
    new_window.configure(bg = BACKGROUND)
    new_window.resizable(False, False)
    
    #frame - columna 1
    frame = tk.Frame(new_window, width = 400, height= 800, bg= LAVANDER)
    frame.place(x=20, y=80)
    
    #contenido frame
    ref = tk.Label(frame, text= "No. Referencia", bg= LAVANDER, fg = DARK_BLUE, font = (FONT, 14, BOLD))
    ref.place(x = 20, y = 45)

  elif (username != USER and password != PASSWORD):
    messagebox.showerror("Error","Datos ingresados incorrectos")
  elif (password != PASSWORD):
    messagebox.showerror("Error","Contraseña incorrecta")
  elif (username != USER):
    messagebox.showerror("Error","Usuario incorrecto")


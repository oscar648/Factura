import tkinter
from tkinter import*
from tkinter import messagebox # alertar y precaucion
import os



"""def pantalla():
    global pantalla"""
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("descarga.ico")

    label=Label(text="Acceso el sistema",bg="navy",fg="white",width="300",height="3",font=("calibri",15)).pack()
    label(text="").pack()
    Button(text="Iniciar Sesión",height="3",width="30", relief=RAISED,\
                             cursor="watch").pack()#la funcion relief sirver para la seleccion  ---cursor="watch" cambiar el curso


    button2=Button(text="Registrate",height="3",width="30", relief=RAISED,\
                             cursor="watch").pack()
    label(text="").pack()
    """def obtener ():
        #print(valor.get())
        messagebox.showinfo("Mensaje","Se alogiado"+valor.get())
    valor=StringVar()"""

    pantalla.mainloop()

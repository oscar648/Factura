import tkinter
from tkinter import*
from tkinter import messagebox


pantalla=Tk()
pantalla.geometry("300x380")
pantalla.title("Bienvenidos")
pantalla.iconbitmap("descarga.ico")

label=Label(text="Acceso el sistema",bg="navy",fg="white",width="300",height="3",font=("calibri",15)).pack()
Button(text="Iniciar Sesión",height="3",width="30", relief=RAISED,\
                         cursor="watch").pack()#la funcion relief sirver para la seleccion  ---cursor="watch" cambiar el curso


Button2(text="Registrate",height="3",width="30", relief=RAISED,\
                         cursor="watch").pack()

pantalla.mainloop()

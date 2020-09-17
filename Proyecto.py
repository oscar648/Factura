from tkinter import *



raiz=Tk()
raiz.title ("ventana")# Título de la ventana

#-------raiz.resizable(0,0)----
raiz.geometry("500x500")
#--------raiz.button.place(X=60, y=40, width=100; height=30)
# raiz  crea la ventana

miFrame=Frame()
miFrame.pack(fill="x")#para expandir o localizar el frame en un lado
miFrame.config(bg="red")#color en el frame
miFrame.config(width="500", height="400")
miFrame.config(bd=35) #combiar el color a mas grueso
miFrame.config(relief="groove") #sombreado para el frame
miFrame.config(cursor="pirate") #cambiar el cursor

# Comenzamos el bucle de aplicación, es como un while True
raiz.mainloop()

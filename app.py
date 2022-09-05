from tkinter import *
import pandas as pd
import datos as dt

root = Tk()
root.title("Ventana principal")
root.geometry("400x150")

etiqueta = Label(root,
                 text="¿Usted es bobo?").grid(row=0, pady=10, padx=10)


siInteresa = Button(root, text="Me interesa", width=50).grid(
    padx=10, pady=10, row=1, column=0, columnspan=2, sticky=E+W)
noInteresa = Button(root, text="No me interesa", width=50).grid(
    padx=10, pady=10, row=2, column=0, columnspan=2, sticky=E+W)
#preguntas = dt.retorno()
#print(preguntas)
mainloop()
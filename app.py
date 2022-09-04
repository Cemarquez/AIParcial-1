from tkinter import *
import pandas as pd
import datos as dt

root = Tk()
root.title("Ventana principal")
root.geometry("400x150")

etiqueta = Label(root,
                 text="Test para identificación de intereses vocacionales y profesionales").grid(row=0, pady=10, padx=10)

preguntas = dt.retorno()
print(preguntas)
#mainloop()
from random import random
import datos as dt
import random
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk

preguntas = dt.retorno()
respuestas = {}
con = 0
print("HOLA")
while con <= 78:
    respuestas[con] = random.randint(0, 1)
    con += 1


def calcular_resultado():
    global respuestas
    calculoArea = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    split = int(len(preguntas)/5)
    conR = 0
    con = 1

    for clave in respuestas:
        calculoArea[con] = calculoArea[con] + respuestas[clave]
        print(clave, split, con)
        if clave == split and con < 5:
            con += 1
            split += int(len(preguntas)/5)

    return calculoArea


root = tk.Tk()
width = 900
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.title("Test Vocacional")
pregunta = tk.Label(root)
pregunta["anchor"] = "center"
ft = tkFont.Font(family='default', size=25)
pregunta["font"] = ft
pregunta["fg"] = "#333333"
pregunta["justify"] = "center"
imgProfesiones = Image.open('profesiones.png')
imgProfesiones = imgProfesiones.resize((900, 400), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgProfesiones = ImageTk.PhotoImage(imgProfesiones)
pregunta["image"] = imgProfesiones
pregunta["wraplength"] = 800
pregunta.place(x=0, y=0)

resultados = ""
calculoArea = calcular_resultado()
for clave in calculoArea:
    
    
respuesta = tk.Label(root)
respuesta["anchor"] = "center"
ft = tkFont.Font(family='default', size=16)
respuesta["font"] = ft
respuesta["fg"] = "#333333"
respuesta["justify"] = "center"
respuesta["wraplength"] = 800
respuesta.place(x=0, y=410)
respuesta["text"] = resultados
root.mainloop()

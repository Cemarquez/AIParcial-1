from calendar import c
from random import random
from turtle import exitonclick
import datos as dt
import random
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk


preguntas = dt.retorno()
respuestas = {}
con = 0
while con <= 78:
    respuestas[con] = random.randint(0, 1)
    con += 1

def close():
   #win.destroy()
   root.quit()
   
def calcular_resultado():
    global respuestas
    calculoArea = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    split = int(len(preguntas)/5)
    conR = 0
    con = 1

    for clave in respuestas:
        calculoArea[con] = calculoArea[con] + respuestas[clave]
        if clave == split and con < 5:
            con += 1
            split += int(len(preguntas)/5)

    return calculoArea


root = tk.Tk()
root.configure(background='white')
width = 900
height = 700
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.title("Test Vocacional")


lblTitulo1 = tk.Label(root, text="Gráfica de profesiones por área. La puntuación más alta indica el área que genera mayor interés en tí.")
lblTitulo1.place(x=10, y=5)  
lblTitulo1.configure(background='white')
lblTitulo1["wraplength"] = 800
ft = tkFont.Font(family='Segoe UI Semibold', size=14)
lblTitulo1["font"] = ft
lblTitulo1["justify"] = "left"

pregunta = tk.Label(root)
imgProfesiones = Image.open('resources/profesiones.png')
imgProfesiones = imgProfesiones.resize((900, 400)) # Redimension (Alto, Ancho)
imgProfesiones = ImageTk.PhotoImage(imgProfesiones)
pregunta["image"] = imgProfesiones
pregunta["wraplength"] = 800
pregunta.place(x=0, y=75)

resultados = ""
calculoArea = calcular_resultado()
for clave in calculoArea:
    if calculoArea[clave] >= 10:
        print ("\033[1m" + 'Hello')
        resultados += "  Área " + str(clave) +": " + str(calculoArea[clave]) + "\n"
    else:
        resultados += "Área " + str(clave) +": " + str(calculoArea[clave]) + "\n"

lblTitulo = tk.Label(root, text = "Los resultados obtenidos fueron: ")
lblTitulo.place(x=10, y=490)
lblTitulo["font"] = ft    
lblTitulo.configure(background='white')



respuesta = tk.Label(root)
ft1 = tkFont.Font(family='Segoe UI', size=12)
respuesta["font"] = ft1
respuesta["fg"] = "#333333"
respuesta["justify"] = "center"
respuesta["wraplength"] = 800
respuesta.place(x=10, y=520)
respuesta["text"] = resultados
respuesta.configure(background='white')

finalizar = tk.Button(text="Finalizar", command = close, background="red",fg="white", font="Segoe 10 ")
finalizar.place(x=400, y=650, width=100, height=35)

root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from turtle import color
import datos as dt
import ctypes  
from tkinter import PhotoImage
from PIL import Image,ImageTk


root = tk.Tk()
root.title("Test Vocacional")
preguntas = dt.retorno()
respuestas = {}
index = 70


def noMeInteresa_command():
        global index
        global preguntas
        global pregunta
        global respuestas
        global progreso
        respuestas[index] = 0
        index+=1
        if index < len(preguntas):
                pregunta["text"] = preguntas[index]
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
        else:
                pregunta["text"] = "Final del Test Vocacional"
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
                print("Aqui va el metodo para entregar resultado")


def meInteresa_command():
        global index
        global preguntas
        global pregunta
        global respuestas
        global progreso
        respuestas[index] = 1
        index+=1
        if index < len(preguntas):
                pregunta["text"] = preguntas[index]
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
        else:
                pregunta["text"] = "Final del Test Vocacional"
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
                print("Aqui va el metodo para entregar resultado")


def atras_command():
        global index
        global preguntas
        global pregunta
        global progreso
        if index != 0 :
                index-=1
                pregunta["text"] = preguntas[index]
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
        else:
               ctypes.windll.user32.MessageBoxW(0, "Se encuentra en la pregunta 1.", "Error", 0)  

def siguiente_command():
        global index
        global preguntas
        global pregunta
        global respuestas
        global progreso

        try:
                respuestas[index]
                index +=1
                pregunta["text"] = preguntas[index]
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
        except:
                ctypes.windll.user32.MessageBoxW(0, "Por favor responda esta pregunta para continuar.", "Pregunta sin contestar", 0)
        

#setting window size
width = 900
height = 600
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

pregunta = tk.Label(root)
pregunta["anchor"] = "center"
ft = tkFont.Font(family='default', size=25)
pregunta["font"] = ft
pregunta["fg"] = "#333333"
pregunta["justify"] = "center"
pregunta["text"] = preguntas[index]
pregunta.place(x=30, y=0, width=863, height=127)

noMeInteresa = tk.Button(root)
noMeInteresa["bg"] = "#f0f0f0"
ft = tkFont.Font(family='default', size=15)
noMeInteresa["font"] = ft
noMeInteresa["fg"] = "#000000"
noMeInteresa["justify"] = "center"
noMeInteresa["bg"] = "SpringGreen2"
noMeInteresa["text"] = "No me interesa"
noMeInteresa.place(x=30, y=220, width=400, height=100)
noMeInteresa["command"] = noMeInteresa_command

meInteresa = tk.Button(root)
meInteresa["bg"] = "#f0f0f0"
ft = tkFont.Font(family='default', size=15)
meInteresa["font"] = ft
meInteresa["fg"] = "#000000"
meInteresa["justify"] = "center"
meInteresa["bg"] = "SpringGreen2"
meInteresa["text"] = "Me interesa"
meInteresa.place(x=470, y=220, width=400, height=100)
meInteresa["command"] = meInteresa_command

atras = tk.Button(root)
atras["bg"] = "#f0f0f0"
ft = tkFont.Font(family='default', size=15)
atras["font"] = ft
atras["fg"] = "#000000"
atras["justify"] = "center"
atras["text"] = "Volver"
atras.place(x=30, y=450, width=100, height=40)
atras["command"] = atras_command

img = Image.open('left.png')
img = img.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
atras["image"] = img

siguiente = tk.Button(root)
siguiente["bg"] = "#f0f0f0"
ft = tkFont.Font(family='default', size=15)
siguiente["font"] = ft
siguiente["fg"] = "#000000"
siguiente["justify"] = "center"
siguiente["text"] = "Siguiente"
siguiente.place(x=770, y=450, width=100, height=40)
siguiente["command"] = siguiente_command

img2 = Image.open('right.png')
img2 = img2.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img2 = ImageTk.PhotoImage(img2)
siguiente["image"] = img2

progreso = tk.Label(root)
ft = tkFont.Font(family='default', size=15)
progreso["font"] = ft
progreso["fg"] = "#333333"
progreso["justify"] = "center"
progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
progreso.place(x=(width/2)-100 , y=460, width=200, height=30)




root.mainloop()
    

import tkinter as tk
import tkinter.font as tkFont
import datos as dt
import ctypes  
from PIL import Image,ImageTk
from tkinter import ttk

root = tk.Tk()
root.title("Test Vocacional")
preguntas = dt.retorno()
respuestas = {}
index = 0

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
                progress()
        else:
                pregunta["text"] = "Final del Test Vocacional"
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
                print("Aqui va el metodo para entregar resultado")
                calcular_resultado()
def close():
   #win.destroy()
   root.quit()

def calcular_resultado():
        global imgProfesiones
        global root
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
                
        for ele in root.winfo_children():
                 ele.destroy()

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


        resultados = ""

        for clave in calculoArea:
                if calculoArea[clave] >= 10:
                        resultados += "  Área " + str(clave) +": " + str(calculoArea[clave]) + "\n"
                else:
                        resultados += "Área " + str(clave) +": " + str(calculoArea[clave]) + "\n"

        lblTitulo = tk.Label(root, text = "Los resultados obtenidos fueron: ")
        lblTitulo.place(x=10, y=490)
        lblTitulo["font"] = ft    
        lblTitulo.configure(background='white')

        
        lblProfesiones = tk.Label(root)
        imgProfesiones = Image.open('resources/profesiones.png')
        imgProfesiones = imgProfesiones.resize((900, 400)) # Redimension (Alto, Ancho)
        imgProfesiones = ImageTk.PhotoImage(imgProfesiones)
        lblProfesiones["image"] = imgProfesiones
        lblProfesiones["wraplength"] = 800
        lblProfesiones.place(x=0, y=75)


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
                progress()
        else:
                pregunta["text"] = "Final del Test Vocacional"
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
                calcular_resultado()


def atras_command():
        global index
        global preguntas
        global pregunta
        global progreso
        if index != 0 :
                index-=1
                pregunta["text"] = preguntas[index]
                progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
                reverse()
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
                progress()
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
root.configure(background='white')
pregunta = tk.Label(root)
pregunta["anchor"] = "center"
ft = tkFont.Font(family='default', size=25)
pregunta["font"] = ft
pregunta["fg"] = "#333333"
pregunta["justify"] = "center"
pregunta["text"] = preguntas[index]
pregunta["wraplength"] = 800
pregunta.place(x=30, y=0, width=863, height=200)
pregunta.configure(background='white')

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

img = Image.open('resources/left.png')
img = img.resize((30, 30)) # Redimension (Alto, Ancho)
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

img2 = Image.open('resources/right.png')
img2 = img2.resize((30, 30)) # Redimension (Alto, Ancho)
img2 = ImageTk.PhotoImage(img2)
siguiente["image"] = img2

progreso = tk.Label(root)
ft = tkFont.Font(family='default', size=15)
progreso["font"] = ft
progreso["fg"] = "#333333"
progreso["justify"] = "center"
progreso["text"] = "Pregunta " + str(index+1) + " / " + str(len(preguntas)+1)
progreso.place(x=(width/2)-100 , y=490, width=200, height=30)
progreso.configure(background='white')



pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
pb.place(x=(width/2)-140, y=460)

# label
value_label = ttk.Label(root, text="a")
value_label.grid(column=0, row=1, columnspan=2)

def progress():
        global pb
        if pb['value'] < 100:
                pb['value'] += 1.25

def reverse():
        global pb
        if pb['value'] < 100:
                pb['value'] -= 1.25


root.mainloop()
    

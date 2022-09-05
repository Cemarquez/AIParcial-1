import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from turtle import color
#import datos as dt

class App:
    def __init__(self, root):
        #setting title
        root.title("Test Vocacional")
        #setting window size
        width=900
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        pregunta=tk.Label(root)
        pregunta["anchor"] = "center"
        ft = tkFont.Font(family='default',size=25)
        pregunta["font"]=ft
        pregunta["fg"] = "#333333"
        pregunta["justify"] = "center"
        pregunta["text"] = "Aquí se debería mostrar la pregunta"
        pregunta.place(x=30,y=0,width=863,height=127)

        noMeInteresa=tk.Button(root)
        noMeInteresa["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='default',size=15)
        noMeInteresa["font"]=ft
        noMeInteresa["fg"] = "#000000"
        noMeInteresa["justify"] = "center"
        noMeInteresa["bg"]= "SpringGreen2"
        noMeInteresa["text"] = "Me interesa"
        noMeInteresa.place(x=30,y=220,width=400,height=100)
        noMeInteresa["command"] = self.noMeInteresa_command

        meInteresa=tk.Button(root)
        meInteresa["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='default',size=15)
        meInteresa["font"]=ft
        meInteresa["fg"] = "#000000"
        meInteresa["justify"] = "center"
        meInteresa["bg"]= "SpringGreen2"
        meInteresa["text"] = "No me interesa"
        meInteresa.place(x=470,y=220,width=400,height=100)
        meInteresa["command"] = self.meInteresa_command

        atras=tk.Button(root)
        atras["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='default',size=15)
        atras["font"]=ft
        atras["fg"] = "#000000"
        atras["justify"] = "center"
        atras["text"] = "Volver"
        atras.place(x=30,y=450,width=100,height=40)
        atras["command"] = self.atras_command

        siguiente=tk.Button(root)
        siguiente["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='default',size=15)
        siguiente["font"]=ft
        siguiente["fg"] = "#000000"
        siguiente["justify"] = "center"
        siguiente["text"] = "Siguiente"
        siguiente.place(x=770,y=450,width=100,height=40)
        siguiente["command"] = self.siguiente_command

        progreso=tk.Label(root)
        ft = tkFont.Font(family='default',size=15)
        progreso["font"]=ft
        progreso["fg"] = "#333333"
        progreso["justify"] = "center"
        progreso["text"] = "Pregunta X"
        progreso.place(x=390,y=460,width=120,height=25)

    def noMeInteresa_command(self):
        print("command")


    def meInteresa_command(self):
        print("command")


    def atras_command(self):
        print("command")


    def siguiente_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

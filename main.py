import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
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
        ft = tkFont.Font(family='Times',size=46)
        pregunta["font"] = ft
        pregunta["fg"] = "#333333"
        pregunta["justify"] = "center"
        pregunta["text"] = "label"
        pregunta.place(x=20,y=20,width=863,height=127)

        noMeInteresa=tk.Button(root)
        noMeInteresa["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        noMeInteresa["font"] = ft
        noMeInteresa["fg"] = "#000000"
        noMeInteresa["justify"] = "center"
        noMeInteresa["text"] = "Button"
        noMeInteresa.place(x=30,y=180,width=400,height=250)
        noMeInteresa["command"] = self.noMeInteresa_command

        meInteresa=tk.Button(root)
        meInteresa["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        meInteresa["font"] = ft
        meInteresa["fg"] = "#000000"
        meInteresa["justify"] = "center"
        meInteresa["text"] = "ButtonButtongcghn"
        meInteresa.place(x=470,y=180,width=400,height=250)
        meInteresa["command"] = self.meInteresa_command

        atras=tk.Button(root)
        atras["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        atras["font"] = ft
        atras["fg"] = "#000000"
        atras["justify"] = "center"
        atras["text"] = "Button"
        atras.place(x=30,y=500,width=60,height=60)
        atras["command"] = self.atras_command

        siguiente=tk.Button(root)
        siguiente["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        siguiente["font"] = ft
        siguiente["fg"] = "#000000"
        siguiente["justify"] = "center"
        siguiente["text"] = "Button"
        siguiente.place(x=810,y=500,width=60,height=60)
        siguiente["command"] = self.siguiente_command

        progreso=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        progreso["font"] = ft
        progreso["fg"] = "#333333"
        progreso["justify"] = "center"
        progreso["text"] = "label"
        progreso.place(x=420,y=520,width=70,height=25)

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

import pandas
import xlrd as xl

def retorno():
    df = pandas.read_excel("Preguntas.xlsx")
    preguntas = []

    for row in df.iterrows():
        preguntas.append(row[1][0])

    return preguntas


    
    

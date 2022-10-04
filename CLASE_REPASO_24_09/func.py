import json


def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["paulina"]

def mostrar(lista:list):
    print("\n")
    for elemento in lista:
        print("{0}-{1}-{2}".formar(elemento["views"],elemento["length"],elemento["title"]))
    print("\n")

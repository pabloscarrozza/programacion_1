import json
import re

def cargar_json(path:str) -> list:
    '''
    Recibe un path donde está ubicado el archivo por parámetro
    Abre el archivo y crea una lista nueva
    Retorna una lista
    '''
    with open(path, "r") as file:
        buffer_dict = json.load(file)
    return buffer_dict['pokemones']

def mostrar_menu() -> None:
    '''
    Muestra un menú numérico en consola
    '''
    mensaje = \
    '''
    1. Listar los últimos N pokemones\n
    2. Ordenar y Listar pokemones por poder ("asc" o "desc")\n
    3. Ordenar y Listar pokemones por ID ("asc" o "desc")\n
    4. \n
    5. \n
    6. \n
    7. Salir\n
    '''
    print(mensaje)

def validar_respuesta(respuesta:str , patron:str) -> int:
    '''
    Recibe por parámetro un string para validar
    Recibe por parámetro un patrón para matchear
    Retorna la respuesta validada o -1 en caso de error
    '''
    if respuesta:
        if re.match(patron, respuesta):
            return respuesta
    return -1

def validar_len_lista(lista:list, tam:int) -> int:
    '''
    Recibe por parámetro una lista
    Recibe por parámetro una cantidad
    Valida que la lista no esté vacía 
    y si la cantidad supera a la longitud de la lista
    '''
    if lista:
        tam = int(tam)
        if tam > 0 and tam < len(lista):
            print(f'Tamaño correcto: {tam}')
            return tam
    print(f'Tamaño máximo erroneo, hay {len(lista)} pokemones')
    return len(lista)




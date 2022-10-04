import json
import re

def cargar_json(path:str) -> list:
    '''
    Recibe un path donde está ubicado el archivo por parámetro
    Abre el archivo y crea una lista nueva
    Retorna una lista
    '''
    buffer_dict = []
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["heroes"]

def imprimir_menu()-> None:
    mensaje =\
    '''
    1 - Listar los primeros N héroes\n
    2 - Ordenar y listar héroes por altura ("asc" o "desc")\n
    3 - Ordenar y listar héroes por fuerza ("asc" o "desc")\n
    4 - Calcular promedio de cualquier key numérica("menor" o "mayor")\n
    5 - Buscar héroes por inteligencia\n
    6 - Exportar a CSV la lista según opción elegida anteriormente [1-4]\n
    7 - Salir\n
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

def validar_len_lista(lista:list[dict], tam:int) -> int:
    '''
    Recibe por parámetro una lista a validar
    Recibe por parámetro un tamaño a validar
    Retorna el tamaño correcto o el largo de la lista si es incorrecto
    '''
    if lista:
        tam = int(tam)
        if tam > 0 and tam < len(lista):
            print(f'Tamaño correcto: {tam}')
            return tam
    print(f'Tamaño máximo erroneo, hay {len(lista)} héroes')
    return len(lista)

def mostrar(lista:list, key:str = 'fuerza') -> None:
    if lista:
        print("\n")
        for heroe in lista:
            #mensaje = f'Nombre: {heroe["nombre"]} | Identidad: {heroe["identidad"]} | {key.capitalize()}: {heroe[key]}'
            #print(mensaje)
            print("Nombre: {0} | Identidad: {1} | {2}: {3}"\
            .format(heroe["nombre"],heroe["identidad"],key.capitalize(),heroe[key]))
        print("\n")

def buscar_min_max(lista:list, key:str, order:str) -> int:
    '''
    Busca un minimo en una lista de elementos dict con clave [key]
    Recibe una lista de elementos dict con clave -key- y la clave 
    Retorna el indice del elemnto minimo o -1 en caso de error
    '''
    retorno = -1
    if(len(lista) > 0):
        i_min_max = 0
        for i in range(len(lista)):
            if(order == "asc" and lista[i][key] < lista[i_min_max][key])\
            or(order == "desc" and lista[i][key] > lista[i_min_max][key]):
                i_min_max = i
        retorno = i_min_max
    return retorno

def ordenar_heroes(lista:list, key:str, order:str) -> list:
    lista_a_ordenar = lista.copy()
    lista_ordenada = []
    while len(lista_a_ordenar) > 0:
        index_min_max = buscar_min_max(lista_a_ordenar,key,order)
        elemento = lista_a_ordenar.pop(index_min_max)
        lista_ordenada.append(elemento)
    return lista_ordenada

def calcular_promedio(lista:list, key:str) -> int:
    acumulador = 0
    contador = 0
    for heroe in lista:
        acumulador += heroe[key]
        contador += 1
    promedio = acumulador/contador
    return promedio

def ordenar_promedio(lista:list, key:str, order:str) -> list:
    if type(lista[0][key]) != str:
        lista_promedio = []
        for elementos in lista:
            if (order == 'menor' and elementos[key] < calcular_promedio(lista, key))\
            or (order == 'mayor' and elementos[key] > calcular_promedio(lista, key)):
                lista_promedio.append(elementos)
        return lista_promedio
    return -1

def exportar_lista(lista:list):
    '''
    Recibe por parametros una lista
    Exporta la lista ingresada a un archivo csv.
    '''
    with open("CLASE_10/archivo.csv", "w") as file:
        mensaje = ""
        for heroe in lista:
            mensaje += "Nombre: {0}, Identidad: {1}, Altura: {2}, Peso: {3}, Fuerza: {4}, Inteligencia: {5}\n"\
                .format(heroe["nombre"], heroe["identidad"],heroe["altura"],heroe["peso"],
                heroe["fuerza"], heroe["inteligencia"])
        file.write(mensaje)



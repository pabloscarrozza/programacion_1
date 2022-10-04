import re
import json

def imprimir_dato(dato:str) -> str:
    '''
    Recibe por parámetro un string y lo imprime por consola.
    '''
    if(type(dato) == type('')):
        print(dato)
    else:
        print("El tipo de dato recibido no es un string")
# 1.1
def imprimir_menu_desafio_5():
    imprimir_dato(
        'A - Nombres de los Héroes de género M\n'
        'B - Nombres de los Héroes de género F\n'
        'C - Héroe más alto de género M\n'
        'D - Héroe más alto de género F\n'
        'E - Héroe más bajo de género M\n'
        'F - Héroe más bajo de género F\n'
        'G - Promedio de altura de género M\n'
        'H - Promedio de altura de género F\n'
        'I - Cantidad de héroes por color de ojos\n'
        'J - Cantidad de héroes por color de pelo\n'
        'K - Cantidad de héroes por inteligencia\n'
        'L - Lista de héroes por color de ojos\n'
        'M - Lista de héroes por color de pelo\n'
        'N - Lista de héroes por inteligencia\n'
        'Z - Salir\n'
        )
# 1.2
def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    retorno = input('Ingrese una letra (a - o) (Z para salir): ')
    retorno = retorno.upper()
    if re.match('^[A-OZ]{1}$',retorno): # ^ (el sombrerito chino es ALT+94)
        return retorno
    return -1
# 1.3
def star_marvel_app_5(lista_heroes:list):
    while True:
        retorno = stark_menu_principal_desafio_5()
        print(retorno)
        if retorno == 'A':
            pass
        elif retorno == 'B':
            pass
        elif retorno == 'C':
            pass
        elif retorno == 'D':
            pass
        elif retorno == 'E':
            pass
        elif retorno == 'F':
            pass
        elif retorno == 'G':
            pass
        elif retorno == 'H':
            pass
        elif retorno == 'I':
            pass
        elif retorno == 'J':
            pass
        elif retorno == 'K':
            pass
        elif retorno == 'L':
            pass
        elif retorno == 'M':
            pass
        elif retorno == 'N':
            pass
        elif retorno == 'O':
            pass
        elif retorno == 'Z':
            print('Salir')
            break
# 1.4
def leer_archivo(nombre:str) -> list[dict]:
    with open(nombre, 'r') as archivo:
        resultado = json.load(archivo)
        resultado_dict = dict(resultado)
        resultado_lista = list[dict](resultado_dict['heroes'])
        return resultado_lista
#1.5
def guardar_archivo(nombre:str, datos:str):
    try:
        with open(nombre, 'w+') as archivo:
            archivo.write(datos)
            print('.Se creó el archivo: ' + nombre + '.csv')
            return True
    except OSError: #^  Preguntar como chequear el error
        print('ERROR al crear archivo: ' + nombre)
        return False
    # el nombre pasarlo formateado piola.csv
    # salida es el string que quiero ESCRIBIR en el archivo.
# 1.6
def capitalizar_palabras(datos_entrada:str)->str:
    list_datos = datos_entrada.split(' ')
    lista_union = []
    capi = ''
    cadena = ' '
    for elementos in list_datos:
        #letra_capital = elementos[0].upper()
        #resto_elementos = elementos[1:].lower()
        #union = letra_capital + resto_elementos
        capi = elementos.capitalize()
        lista_union.append(capi)
    resultado = cadena.join(lista_union)
    return resultado
# 1.7
def obtener_nombre_capitalizado(heroe:dict)->str:
    nombre = heroe['nombre']
    resultado = 'Nombre: {0}'.format(capitalizar_palabras(nombre))
    return resultado
# 1.8
def obtener_nombre_y_dato(heroe:dict,key:str)->str:
    if len(key)>0 and key in heroe:
        resultado = '{0} | {1}: {2}'.format(obtener_nombre_capitalizado(heroe),key.capitalize(),heroe[key])
    else:
        print('La key ingresada está vacía / no existe')
    return resultado
# 2.1
def es_genero(heroe:dict, genero:str)->bool:
    genero = heroe['genero']
    if genero == 'M' or genero == 'F' or genero == 'NB':
        return True
# 2.2
def stark_guardar_heroe_genero(lista_heroes:list, genero:str)->bool:
    for personajes in lista_heroes:
        genero = personajes['genero']
        if es_genero(personajes, genero):
            if genero == 'M':
                obtener_nombre_capitalizado(personajes)
                guardar_archivo('heroes_M', 'Nombre: {0} | Género: {1}'.format(personajes['nombre'], genero))
            elif genero == 'F':
                obtener_nombre_capitalizado(personajes)
                guardar_archivo('heroes_F', 'Nombre: {0} | Género: {1}'.format(personajes['nombre'], genero))
            elif genero == 'NB':
                obtener_nombre_capitalizado(personajes)
                guardar_archivo('heroes_NB', 'Nombre: {0} | Género: {1}'.format(personajes['nombre'], genero))
    return True




'''
#   Apuntes Facundo:


def stark_app_desafio_5(lista:list):
    pass



lista_heroes = leer_archivo('C:/Users/pablo/OneDrive/Escritorio/Repo Programacion 1/programacion_1/CLASE_08/data_stark.json')
print(lista_heroes)

for heroe in res:
    print(heroe['nombre'], end=' ')

#stark_app_desafio_5(lista_heroes)
'''

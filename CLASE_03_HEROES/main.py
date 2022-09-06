#   Pablo Scarrozza
from data_stark import lista_personajes
#!  A. Analizar detenidamente el set de datos
#!  B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
#!  C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
#!  D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
#!  E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
#!  F. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
#!  G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
#!  H. Calcular e informar cual es el superhéroe más y menos pesado.
#!  I. Ordenar el código implementando una función para cada uno de los valores informados.
#!  J. Construir un menú que permita elegir qué dato obtener
'''
{
        "nombre": "Howard the Duck",
        "identidad": "Howard (Last name unrevealed)",
        "empresa": "Marvel Comics",
        "altura": "79.349999999999994",
        "peso": "18.449999999999999",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Yellow",
        "fuerza": "2",
        "inteligencia": "average"
    }
'''
def casteo_global():
    #?  Casteo global:
    for personaje in lista_personajes:
        personaje['altura'] = float(personaje['altura'])
        personaje['peso'] = float(personaje['peso'])
        personaje['fuerza'] = int(personaje['fuerza'])

def informar_nombres():
    for personaje in lista_personajes:
        print(personaje['nombre'])

def informar_nombre_y_alturas():
    for personaje in lista_personajes:
        print('Nombre: {0} - Altura: {1:05.2f}'.format(personaje['nombre'],personaje['altura']))

def calcular_altura_maxima():
    heroe_altura_maxima = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['altura'] > heroe_altura_maxima['altura']):
            heroe_altura_maxima = personaje
    print('Héroe más alto:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_maxima['nombre'],heroe_altura_maxima['altura']))

def calcular_altura_minima():
    heroe_altura_minimo = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['altura'] < heroe_altura_minimo['altura']):
            heroe_altura_minimo = personaje
    print('Héroe más bajo:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_minimo['nombre'],heroe_altura_minimo['altura']))

def calcular_promedio_alturas():
    acumulador_altura = 0
    for personaje in lista_personajes:
        acumulador_altura += personaje['altura']
    print('Promedio de altura: {0:0.2f}'.format(acumulador_altura/len(lista_personajes)))

def calcular_peso_maximo():
    heroe_peso_maximo = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['peso'] > heroe_peso_maximo['peso']):
            heroe_peso_maximo = personaje
    print('Héroe más pesado:\nNombre: {0} - Peso: {1:05.2f}'.format(heroe_peso_maximo['nombre'],heroe_peso_maximo['peso']))

def calcular_peso_minimo():
    heroe_peso_minimo = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['peso'] < heroe_peso_minimo['peso']):
            heroe_peso_minimo = personaje
    print('Héroe menos pesado:\nNombre: {0} - Peso: {1:05.2f}'.format(heroe_peso_minimo['nombre'],heroe_peso_minimo['peso']))

casteo_global()

while True:

    print(
        '1 - Nombres de los Héroes\n'
        '2 - Nombres y alturas de los Héroes\n'
        '3 - Héroe más alto\n'
        '4 - Héroe más bajo\n'
        '5 - Promedio de altura\n'
        '6 - Héroe más pesado\n'
        '7 - Héroe menos pesado\n'
        '8 - Salir\n'
    )

    respuesta = int(input('Ingrese el número del menú: '))

    if(respuesta == 1):
        informar_nombres()
    elif(respuesta == 2):
        informar_nombre_y_alturas()
    elif(respuesta == 3):
        calcular_altura_maxima()
    elif(respuesta == 4):
        calcular_altura_minima()
    elif(respuesta == 5):
        calcular_promedio_alturas()
    elif(respuesta == 6):
        calcular_peso_maximo()
    elif(respuesta == 7):
        calcular_peso_minimo()
    elif(respuesta == 8):
        break




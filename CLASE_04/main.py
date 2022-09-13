#   Pablo Scarrozza
from data_stark import lista_personajes
'''
A   Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.
B   Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F.
C   Recorrer la lista y determinar cuál es el superhéroe más alto de género M.
D   Recorrer la lista y determinar cuál es el superhéroe más alto de género F.
E   Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M.
F   Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F.
G   Recorrer la lista y determinar la altura promedio de los superhéroes de género M.
H   Recorrer la lista y determinar la altura promedio de los superhéroes de género F.
I   Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F).
J   Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K   Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L   Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con 'No Tiene').
M   Listar todos los superhéroes agrupados por color de ojos.
N   Listar todos los superhéroes agrupados por color de pelo.
O   Listar todos los superhéroes agrupados por tipo de inteligencia.

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

#!  A:
def informar_nombres_m():
    for personaje in lista_personajes:
        if(personaje['genero'] == 'M'):
            print('Héroes:\n',personaje['nombre'])

#!  B:
def informar_nombres_f():
    for personaje in lista_personajes:
        if(personaje['genero'] == 'F'):
            print('Heroínas:\n',personaje['nombre'])

#!  C:
def calcular_altura_maxima_m():
    heroe_altura_maxima_m = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['genero'] == 'M'):
            if(personaje['altura'] > heroe_altura_maxima_m['altura']):
                heroe_altura_maxima_m = personaje
    print('Héroe más alto:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_maxima_m['nombre'],heroe_altura_maxima_m['altura']))

#!  D:
def calcular_altura_maxima_f():
    heroe_altura_maxima_f = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['genero'] == 'F'):
            if(personaje['altura'] > heroe_altura_maxima_f['altura']):
                heroe_altura_maxima_f = personaje
    print('Heroína más alta:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_maxima_f['nombre'],heroe_altura_maxima_f['altura']))

#!  E:
def calcular_altura_minima_m():
    heroe_altura_minimo_m = lista_personajes[0]
    for personaje in lista_personajes:
        if(personaje['genero'] == 'M'):
            if(personaje['altura'] < heroe_altura_minimo_m['altura']):
                heroe_altura_minimo_m = personaje
    print('Héroe más bajo:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_minimo_m['nombre'],heroe_altura_minimo_m['altura']))

#!  F:
def calcular_altura_minima_f():
    heroe_altura_minimo_f = lista_personajes[3]
    for personaje in lista_personajes:
        if(personaje['genero'] == 'F'):
            if(personaje['altura'] < heroe_altura_minimo_f['altura']):
                heroe_altura_minimo_f = personaje
    print('Heroína más baja:\nNombre: {0} - Altura: {1:05.2f}'.format(heroe_altura_minimo_f['nombre'],heroe_altura_minimo_f['altura']))

#!  G:
def calcular_promedio_alturas_m():
    acumulador_altura_m = 0
    contador_altura_m = 0
    for personaje in lista_personajes:
        if(personaje['genero'] == 'M'):
            acumulador_altura_m += personaje['altura']
            contador_altura_m += 1
    print('Promedio de altura de Héroes: {0:0.2f}'.format(acumulador_altura_m/contador_altura_m))

#!  H:
def calcular_promedio_alturas_f():
    acumulador_altura_f = 0
    contador_altura_f = 0
    for personaje in lista_personajes:
        if(personaje['genero'] == 'F'):
            acumulador_altura_f += personaje['altura']
            contador_altura_f += 1
    print('Promedio de altura de Heroínas: {0:0.2f}'.format(acumulador_altura_f/contador_altura_f))

#!  J (otra forma):
'''def cantidad_color_ojos():
    lista_color_ojos = []
    for personaje in lista_personajes:
        lista_color_ojos.append(personaje['color_ojos'])
    lista_color_ojos = list(set(lista_color_ojos))

    for color in lista_color_ojos:
        cantidad_heroes = 0
        for personaje in lista_personajes:
            if personaje['color_ojos'] == color:
                cantidad_heroes += 1
        print(f'Ojos color {color} y cantidad {cantidad_heroes}')'''

#!  J:
def cantidad_color_ojos():
    dict_ojos = {}
    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        if color_ojos not in dict_ojos.keys():
            dict_ojos[color_ojos] = 1
        else:
            dict_ojos[color_ojos] += 1
    for color in dict_ojos.items():
        print('Color: {0} - Cantidad {1}'.format(color[0], color[1]))

#!  K:
def cantidad_color_pelo():
    dict_pelo = {}
    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo not in dict_pelo.keys():
            dict_pelo[color_pelo] = 1
        else:
            dict_pelo[color_pelo] += 1
    for color in dict_pelo.items():
        print('Color: {0} - Cantidad {1}'.format(color[0], color[1]))

#!  L:
def cantidad_inteligencia():
    dict_inteligencia = {}
    for personaje in lista_personajes:
        if len(personaje['inteligencia']) == 0:
            personaje['inteligencia'] = 'No Tiene'
        intel_key = personaje['inteligencia']
        if intel_key not in dict_inteligencia.keys():
            dict_inteligencia[intel_key] = 1
        else:
            dict_inteligencia[intel_key] += 1
    for inteligencia in dict_inteligencia.items():
        print('Inteligencia: {0} - Cantidad {1}'.format(inteligencia[0], inteligencia[1]))

#!  M:
def lista_heroes_color_ojos():
    dict_ojos_nombres = {}
    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        if color_ojos not in dict_ojos_nombres.keys():
            dict_ojos_nombres[color_ojos] = [personaje['nombre']]
        else:
            lista_actual = list(dict_ojos_nombres[color_ojos])
            lista_actual.append(personaje['nombre'])
            dict_ojos_nombres[color_ojos] = lista_actual
            #list(dict_ojos_nombres[color_ojos]).append(personaje['nombre'])
    for color in dict_ojos_nombres.items():
        print('Color de ojos {0} - Nombre {1}'.format(color[0], color[1]))

#!  N:
def lista_heroes_color_pelo():
    dict_pelo_nombres = {}
    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo not in dict_pelo_nombres.keys():
            dict_pelo_nombres[color_pelo] = [personaje['nombre']]
        else:
            lista_actual = list(dict_pelo_nombres[color_pelo])
            lista_actual.append(personaje['nombre'])
            dict_pelo_nombres[color_pelo] = lista_actual
    for color in dict_pelo_nombres.items():
        print('Color de pelo {0} - Nombre {1}'.format(color[0], color[1]))

#!  O:
def lista_heroes_inteligencia():
    dict_intel_nombres = {}
    for personaje in lista_personajes:
        if len(personaje['inteligencia']) == 0:
            personaje['inteligencia'] = 'No Tiene'
        intel_key = personaje['inteligencia']
        if intel_key not in dict_intel_nombres.keys():
            dict_intel_nombres[intel_key] = [personaje['nombre']]
        else:
            lista_actual = list(dict_intel_nombres[intel_key])
            lista_actual.append(personaje['nombre'])
            dict_intel_nombres[intel_key] = lista_actual
    for color in dict_intel_nombres.items():
        print('Inteligencia {0} - Nombre {1}'.format(color[0], color[1]))


casteo_global()

while True:

    print(
        '1 - Nombres de los Héroes\n'
        '2 - Nombres de las Heroínas\n'
        '3 - Héroe más alto\n'
        '4 - Heroína más alta\n'
        '5 - Héroe más bajo\n'
        '6 - Heroína más baja\n'
        '7 - Promedio de altura de Héroes\n'
        '8 - Promedio de altura de Heroínas\n'
        '9 - Cantidad colores de ojos\n'
        '10 - Cantidad colores de pelo\n'
        '11 - Cantidad de Inteligencias\n'
        '12 - Lista de Héroes agrupados por color de ojos\n'
        '13 - Lista de Héroes agrupados por color de pelo\n'
        '14 - Lista de Héroes agrupados por inteligencia\n'
        '15 - Salir\n\n'
    )

    respuesta = int(input('Ingrese el número del menú: '))

    if(respuesta == 1):
        informar_nombres_m()
    elif(respuesta == 2):
        informar_nombres_f()
    elif(respuesta == 3):
        calcular_altura_maxima_m()
    elif(respuesta == 4):
        calcular_altura_maxima_f()
    elif(respuesta == 5):
        calcular_altura_minima_m()
    elif(respuesta == 6):
        calcular_altura_minima_f()
    elif(respuesta == 7):
        calcular_promedio_alturas_m()
    elif(respuesta == 8):
        calcular_promedio_alturas_f()
    elif(respuesta == 9):
        cantidad_color_ojos()
    elif(respuesta == 10):
        cantidad_color_pelo()
    elif(respuesta == 11):
        cantidad_inteligencia()
    elif(respuesta == 12):
        lista_heroes_color_ojos()
    elif(respuesta == 13):
        lista_heroes_color_pelo()
    elif(respuesta == 14):
        lista_heroes_inteligencia()
    elif(respuesta == 15):
        break
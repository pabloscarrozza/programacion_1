#   Pablo Scarrozza
from data_stark import lista_personajes
from calculos import stark_normalizar_datos
from calculos import stark_imprimir_nombres_heroes
from calculos import stark_imprimir_nombres_alturas
from calculos import stark_calcular_imprimir_heroe

#  A. Analizar detenidamente el set de datos
#  B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
#  C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
#  D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
#  E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
#  F. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
#  G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
#  H. Calcular e informar cual es el superhéroe más y menos pesado.
#  I. Ordenar el código implementando una función para cada uno de los valores informados.
#  J. Construir un menú que permita elegir qué dato obtener
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

while True:

    print(
        '0 - Normalizar datos\n'
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

    if(respuesta == 0):
        stark_normalizar_datos(lista_personajes)
    if(respuesta == 1):
        stark_imprimir_nombres_heroes(lista_personajes)
    elif(respuesta == 2):
        stark_imprimir_nombres_alturas(lista_personajes)
    elif(respuesta == 3):
        stark_calcular_imprimir_heroe(lista_personajes, 'altura', 'maximo')
    elif(respuesta == 4):
        stark_calcular_imprimir_heroe(lista_personajes, 'altura', 'minimo')
    elif(respuesta == 5):
        pass
    elif(respuesta == 6):
        pass
    elif(respuesta == 7):
        pass
    elif(respuesta == 8):
        break




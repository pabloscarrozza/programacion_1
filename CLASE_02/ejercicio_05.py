'''Ejercicio Integrador 05

En la base de datos de la división de armamento de industrias Wayne se tiene una 
información la cual están con la necesidad de cambiar el formato la lista de 
habilidades con sus respectivos puntos de combate, actualmente cada una de ellas 
está presente como un diccionario pero para su nuevo sistema requieren que el 
tipo de dato sea una tupla la cual albergue solamente el nombre de la habilidad 
y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de las habilidades 
deben estar dentro de una lista de habilidades, la cual debe ser el valor de una key 
que conforme un diccionario, como key par albergarlas usaremos “habilidades_UTN”.
Formato de resultado esperado:
'''

'''Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,  conjuntamente 
con la key que integra dicha estructura de datos.

EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.
'''

habilidades_UTN = {
    "habilidades_UTN": [("Vuelo", 32), ("Vision-X", 64), ("Super Velocidad", 128), 
    ("Inteligencia", 256), ("Magia", 512), ("Metamorfosis", 1024)]
    }



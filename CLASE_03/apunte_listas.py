QTY_EMPLEADOS = 3

lista_empleados = []

for i in range(QTY_EMPLEADOS):
    dic_empleado = {}
    nombre = input("N?")
    apellido = input("A?")
    dni = input("dni?")
    dic_empleado["nombre"] = nombre
    dic_empleado["apellido"] = apellido
    dic_empleado["dni"] = dni
    lista_empleados.append(dic_empleado)

for empleado in lista_empleados:
    print(empleado["nombre"])


'''
[0] NOMBRE - APELLIDO
[1] NOMBRE - APELLIDO
[2] NOMBRE - APELLIDO
'''
lista_nombres = []
lista_apellidos = []

i = 0
for nombre in range(QTY_EMPLEADOS):
    print("{0} - {1} - {2}".format(i,lista_nombres[i],lista_apellidos[i]))



    #   Pablo Scarrozza
'''

'''

terminal_str = "eeeee123.87"
# Bloque parecido al IF
try: # Tratar
    peso = int(terminal_str)
except: # Si no puede, entra acá
    print('Error')

lista = [1, "Hola", 3.67]
print(lista [1])

lista.append(1)     # Agrega un 1 a la lista

lista[1]    # Muesta una posicion en la lista, en este caso la 2da posicion
lista[3:5]  # Muesta un rango de una lista, en este caso de la posicion 4ta a la 6ta
lista[-1]   # en negativo deja recorrer para atras una lista, en este caso -1 es la última posición de la lista

for i in lista:     # así se recorre una lista
    print(i)

#ejemplo:
lista_temas = ["T1", "T2"]
for tema in lista_temas:    # describir el elemento que agarramos de la lista, depende de qué sea
    print(tema)



lista = tuple([1, "Hola", 3.67])    # Lista inmutable, no la puedo modificar

diccionario = {'nombre' : 'Juan', 'edad' : 21}
print(diccionario['nombre'])    # Juan
print(diccionario['edad'])  # 21

#Set: conjunto de elementos que no pueden estar repetidos

s = {2, 4, 7, 1, 8, 1}
print(s)    # [1, 2, 4, 7, 8]

lista = [1, 3, 6, 3, 2, 1]
s = set(lista)
print(s)    # {1, 2, 3, 6}
print(type(s))  # <class 'set>

dic = {}    # Se crea un diccionario, en este caso, vacío
dic["clave"] = "valor"
dic["nombre"] = "Juan"
# Los diccionarios se pueden recorrer y se pueden iterar

lista=[]

len(lista)      # Para saber cuánto mide una lista

QTY_EMPLEADOS = 3
lista_nombres = []
lista_apellidos = []
for i in range(QTY_EMPLEADOS):
    nombre = input("N?")
    apellido = input("A?")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

'''
[0] NOMBRE - APELLIDO
[1] NOMBRE - APELLIDO
[2] NOMBRE - APELLIDO
'''
i = 0
for nombre in range(QTY_EMPLEADOS):
    print("{0} - {1} - {2}".format(i,lista_nombres[i],lista_apellidos[i]))



def calcular_minimo_maximo(lista_personajes:list,key:str,tipo:str) -> dict:
    '''
    Calcula el valor maximo/minimo en funcion a la key recibida
    de una lista de personajes

    Recibe una lista de diccionarios y la key que se utilizará para calcular
    y el tipo de calculo a realizar ("maximo" o "minimo")

    Retorna el diccionario que contienene el maximo/minimo
    Retorna -1 en caso de error
    '''
    personaje_max_min = -1
    if(type(lista_personajes) == type([]) and type(key) == type('') and len(lista_personajes) > 0):
        personaje_max_min = lista_personajes[0]
        for personaje in lista_personajes:
            if(tipo == 'maximo' and personaje[key] > personaje_max_min[key]):
                personaje_max_min = personaje
            if(tipo == 'minimo' and personaje[key] < personaje_max_min[key]):
                personaje_max_min = personaje
        return personaje_max_min

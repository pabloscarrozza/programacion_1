#   Pablo Scarrozza
# A
def stark_normalizar_datos(lista_personajes:list):
    '''
    Normaliza los datos convirtiendo los strings a flotantes o enteros
    para poder calcularlos.
    Si la lista se encuentra vacía, printea un mensaje de error.
    '''
    if(len(lista_personajes) > 0):
        mensaje = ''
        for personaje in lista_personajes:
            if(type(personaje['altura']) != type(float())):
                personaje['altura'] = float(personaje['altura'])
                mensaje = 'Datos normalizados'
            elif(type(personaje['peso']) != type(float())):
                personaje['peso'] = float(personaje['peso'])
                mensaje = 'Datos normalizados'
            elif(type(personaje['fuerza']) != type(int())):
                personaje['fuerza'] = int(personaje['fuerza'])
                mensaje = 'Datos normalizados'
        if(mensaje == 'Datos normalizados'):
            print(mensaje)
    else:
        print('Error: Lista de héroes vacía')

# B
def obtener_nombre(personaje:dict) -> str:
    '''
    Obtiene los nombres de todos los personajes de la lista.
    Recibe por parámetro un diccionario.
    Retorna el nombre del personaje formateado.
    '''
    return 'Nombre: {0}'.format(personaje['nombre'])

def imprimir_dato(dato:str) -> str:
    '''
    Recibe por parámetro un string y lo imprime por consola.
    '''
    if(type(dato) == type('')):
        print(dato)
    else:
        print("El tipo de dato recibido no es un string")

def stark_imprimir_nombres_heroes(lista_personajes:list):
    '''
    Recibe por parámetro la lista de héroes e imprime
    la lista de nombres.
    '''
    if(len(lista_personajes) > 0):
        for personaje in lista_personajes:
            imprimir_dato(obtener_nombre(personaje))
    else:
        print("Lista vacía")

# C
def obtener_nombre_y_dato(personaje:dict,key:str) -> str:
    '''
    Obtiene por parámetro un diccionario que representa a un héroe
    y una key (str) la cual representará el dato que se desea
    El resultado se muestra formateado
    '''
    if(type(personaje[key]) == type('')):
        personaje[key] = float(personaje[key])
    return 'Nombre: {0} | {1}: {2:05.2f} '.format(personaje['nombre'],key,personaje[key])

def stark_imprimir_nombres_alturas(lista_personajes:list):
    '''
    Recibe por parámetro la lista de héroes e imprime
    la lista de nombres junto a su key 'altura' y su valor
    '''
    if(len(lista_personajes) > 0):
        for personaje in lista_personajes:
            print(obtener_nombre_y_dato(personaje,'altura'))
    else:
        print("Lista vacía")

# D
def calcular_max(lista_personajes:list,key:str):
    '''
    Recibe una lista de diccionarios y la key que se utilizará para calcular
    el máximo
    Retorna el diccionario que contiene el máximo
    Retorna -1 en caso de error
    '''
    personaje_max = -1
    if(type(lista_personajes) == type([]) and type(key) == type('') and len(lista_personajes) > 0):
        personaje_max = lista_personajes[0]
        for personaje in lista_personajes:
            if(type(personaje[key]) == type('')):
                personaje[key] = float(personaje[key])
            if(personaje[key] > personaje_max[key]):
                personaje_max = personaje
        return personaje_max

# E
def calcular_min(lista_personajes:list,key:str):
    '''
    Recibe una lista de diccionarios y la key que se utilizará para calcular
    el mínimo
    Retorna el diccionario que contiene el mínimo
    Retorna -1 en caso de error
    '''
    personaje_min = -1
    if(type(lista_personajes) == type([]) and type(key) == type('') and len(lista_personajes) > 0):
        personaje_min = lista_personajes[0]
        for personaje in lista_personajes:
            if(type(personaje[key]) == type('')):
                personaje[key] = float(personaje[key])
            if(personaje[key] < personaje_min[key]):
                personaje_min = personaje
        return personaje_min

def calcular_max_min_dato(lista_personajes:list,key:str,tipo:str):
    '''
    Recibe una lista de diccionarios, la key que se utilizará para calcular
    el mínimo o el maximo y el tipo ("maximo o minimo")
    Retorna el diccionario que contiene el mínimo o el maximo
    Retorna -1 en caso de error
    '''
    if(tipo == 'maximo'):
        calcular_max(lista_personajes,key)
    elif(tipo == 'minimo'):
        calcular_min(lista_personajes,key)

def stark_calcular_imprimir_heroe(lista_personajes:list,key:str,tipo:str):
    '''
    
    '''
    if(len(lista_personajes) > 0):
        print(calcular_max_min_dato(lista_personajes,key,tipo))

'''
def calcular_promedio_alturas():
    acumulador_altura = 0
    for personaje in lista_personajes:
        acumulador_altura += personaje['altura']
    print('Promedio de altura: {0:0.2f}'.format(acumulador_altura/len(lista_personajes)))
'''

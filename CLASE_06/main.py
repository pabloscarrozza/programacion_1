from data import lista_personajes

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
    "inteligencia": ""
}
'''


def extraer_iniciales(nombre_heroe:str) -> str:
    '''
    Extrae las iniciales de los nombres.
    Si el nombre contiene 'the', se omite.
    Si el nombre contiene '-', se reemplaza por un espacio en blanco.
    Recibe como parametro un str.
    Retorna un str.
    '''
    iniciales = ''
    if(len(nombre_heroe)> 0):
        if(nombre_heroe.count('the')>0):
            nombre_heroe = nombre_heroe.replace('the ','')
        if(nombre_heroe.count('-')>0):
            nombre_heroe = nombre_heroe.replace('-',' ')
        lista_palabras = nombre_heroe.split(' ')
        for palabra in lista_palabras:
            iniciales += '{0}.'.format(palabra[:1].upper())
    else:
        return 'N/A'
    return iniciales

#print(extraer_iniciales('Iron Man'))

def definir_iniciales_nombre(heroe:dict) -> bool:
    retorno = False
    if(type(heroe) == type({}) and 'nombre' in heroe.keys()):
        key = 'iniciales'
        value = extraer_iniciales(lista_personajes['nombre'])
        heroe[key] = value
        retorno = True
    return retorno

#print(definir_iniciales_nombre())

def agregar_iniciales_nombre(lista_heroes:list) -> bool:
    if(len(lista_heroes)>0 and type(lista_heroes) == type([])):
        for personajes in lista_heroes:
            if(definir_iniciales_nombre(personajes) == False):
                print('El origen de datos no contiene el formato correcto')
            else:
                definir_iniciales_nombre(personajes)
    return True

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if(len(lista_heroes)>0 and type(lista_heroes)==type([])):
        for personajes in lista_heroes:
            agregar_iniciales_nombre(lista_heroes)
            print('* {0} ({1})'.format(lista_heroes['nombre'], extraer_iniciales(personajes)))

#stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int):
    if type(id_heroe) == type(int()):
        for personajes in lista_personajes:
            if personajes['genero'] == 'M' or personajes['genero'] == 'F' or personajes['genero'] == 'NB':
                genero_heroe = personajes['genero']
                if len(genero_heroe) == 1:
                    if len(str(id_heroe)) == 1:
                        print('{0}-0000000{1}'.format(genero_heroe, id_heroe))
                    elif len(str(id_heroe)) == 2:
                        print('{0}-000000{1}'.format(genero_heroe, id_heroe))
                else:
                    if len(str(id_heroe)) == 1:
                        print('{0}-000000{1}'.format(genero_heroe, id_heroe))
                    elif len(str(id_heroe)) == 2:
                        print('{0}-00000{1}'.format(genero_heroe, id_heroe))
            else:
                print('N/A')
    else:
        print('N/A')

def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    retorno = False
    if len(heroe) > 0: # and generar_codigo_heroe(id_heroe) == 10:
        key = 'codigo_heroe'
        value = generar_codigo_heroe(id_heroe)
        heroe[key] = value
        retorno = True
    return retorno

def stark_generar_codigos_heroes(lista_heroes:list):
    if len(lista_heroes) > 0:
        contador = 0
        for personajes in lista_heroes:
            if type(personajes) == type({}):
                if personajes['genero'] in lista_heroes:
                    contador += 1
                    id_heroe = contador
                    agregar_codigo_heroe(personajes, id_heroe)
        print('Se asignaron {0} códigos'.format(contador))

#print(stark_generar_codigos_heroes(lista_personajes))

#def sanitizar_entero(numero_str:str):





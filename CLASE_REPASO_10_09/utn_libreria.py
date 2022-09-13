''' {
        "id": 1,
        "nombre": "bulbasaur",
        "tipo": ["planta"],
        "evoluciones": ["ivysaur", "venusaur"],
        "poder": 4,
        "fortaleza":["agua"],
        "debilidad":["fuego"]
    },'''

def obtener_nombre_pokemon(pokemon: dict) -> str:
    '''
    Recibe

    Parametros: El diccionario de pokemones
    Retorno: El nombre del pokemon
    '''
    return pokemon['nombre']

def imprimir_pokemones(pokemones: list) -> None:
    '''
    Recibe la lista de pokemones, obtiene el nombre de cada uno
    y los imprime uno a uno.

    Parametros: La lista de diccionarios de pokemones
    Retorno: None
    '''
    if len(pokemones) > 0:
        for pokemon in pokemones:
            nombre = obtener_nombre_pokemon(pokemon)
            print(nombre)

def tiene_id_par(pokemon: dict) -> bool:
    '''
    Recibe un diccionario de pokemones, obtiene True si
    el ID del pokemon es par.
    
    Parametros: El diccionario de pokemones.
    Retorno: True si el ID del pokemon es par,
    False si el ID del pokemon es impar.
    '''
    if int(pokemon['id']) % 2 == 0:
        return True
    return False

def obtener_id_pokemon(pokemon: dict) -> str:
    '''
    Recibe un diccionario de pokemones, obtiene el ID del pokemon.

    Parametros: El diccionario de pokemones.
    Retorno: el id como string
    '''









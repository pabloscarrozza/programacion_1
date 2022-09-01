#   Pablo Scarrozza

'''Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento 
de HR dispone de una larga lista de justicieros pero solo tiene información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 'heroes_para_reclutar' 
busque en el diccionario 'heroes_info' los que coincidan y los guarde en un nuevo diccionario para luego 
imprimir por consola todos sus datos. (id, origen, etc)
TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan duplicados, 
que usarías para eso?
'''

heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]

heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

for heroe in heroes_para_reclutar:
    # Iterar cada heroe y verificar que exista en el dic.
    if heroe in heroes_info.keys():
        # El metodo .keys devuelve True si lo que evaluo dentro del dicc Existe como Clave / Key
        info_heroe = heroes_info[heroe]
        # Traemos cada uno de sus datos
        id = info_heroe["ID"]
        origen = info_heroe["Origen"]
        identidad = info_heroe["Identidad"]
        habilidades_lista = info_heroe["Habilidades"]

        # Eliminar duplicados
        # Pase la lista a set para borrar repetidos
        habilidades_unicas = set(habilidades_lista)
        # Pase el set a lista porque quiero iterar una lista
        habilidades_unicas_lista = list(habilidades_unicas)
        
        habilidades_str = ' | '.join(habilidades_unicas_lista)
        print("ID:", id, ", Codename:", heroe)
        print("Identidad:", identidad, ", Origen:", origen)
        print("Habilidades:", habilidades_str)
        print("----------------------------------------", "\n")
        

'''
        mensaje = ''
        for habilidad in habilidades_lista_otra:
            mensaje += ' {0}'.format(habilidad)
        
        print(id)
        print(origen)
        print(identidad)
        print(mensaje)
'''

#print("{0} - {1} - {2} - {3} - {4}".format(heroe, id, origen, identidad, mensaje))




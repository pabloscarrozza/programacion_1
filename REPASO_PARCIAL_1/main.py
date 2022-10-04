'''
1. Listar los últimos N pokemones. El valor de N será ingresado por el usuario 
(Validar que no supere max. de lista)

2. Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar 
de manera ascendente ("asc") o descendente ("desc")

3. Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de 
manera ascendente ("asc") o descendente ("desc")

4. Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo), 
filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: 
"menor" o "mayor") se deberá listar en consola aquellos que cumplan con tener mayores o menores cantidades 
en la lista de dicha key según corresponda.

5. Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer, muchos de ellos 
poseen más de un tipo, con lo cual habrá que darle a elegir al usuario entre todos los tipos que existen 
en el json) una vez seleccionado listar en consola los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, 
deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).

6. Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

{
    "id": 1,
    "nombre": "bulbasaur",
    "tipo": ["planta"],
    "evoluciones": ["ivysaur", "venusaur"],
    "poder": 4,
    "fortaleza":["agua"],
    "debilidad":["fuego"]
}
'''
import funciones as func

def pokemon_app():
    lista_pokemones = func.cargar_json("C:/Users/pablo/OneDrive/Escritorio/Repo Programacion 1/programacion_1/REPASO_PARCIAL_1/pokedex.json")
    lista_a_archivo = []
    while True:
        func.mostrar_menu()
        respuesta = func.validar_respuesta(input("Ingrese una opción (1 al 7): "), "^[1-7]{1}$")
        while respuesta == -1:
            respuesta = func.validar_respuesta(input("ERROR! Ingrese una opción válida (1 al 7): "), "^[1-7]{1}$")
        if respuesta == "1":
            respuesta = input("Ingrese la cantidad de pokemones a listar: ")
            cantidad = int(func.validar_respuesta(respuesta, "^[1-9]{1,2}$"))
            cantidad = func.validar_len_lista(lista_pokemones, cantidad)
        elif respuesta == "2":
            print("Está en la opción 2")
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            pass
        elif respuesta == "5":
            pass
        elif respuesta == "6":
            pass
        elif respuesta == "7":
            print("Hasta luego!")
            break




pokemon_app()

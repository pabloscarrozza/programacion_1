'''
1. Listar los primeros N héroes. El valor de N será ingresado por el usuario 
(Validar que no supere max. de lista)

2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera
ascendente ("asc") o descendente ("desc")

3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera
ascendente ("asc") o descendente ("desc")

4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de
superar o no el promedio (preguntar al usuario la condición: "menor" o "mayor") se deberá
listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

5. Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan
dicha búsqueda.

6. Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones,
validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "altura": 79.35,
    "peso": 18.45,
    "fuerza": 2,
    "inteligencia": ""
}
'''
import funciones as func

def heroes_app():
    lista_heroes = func.cargar_json("C:/Users/pablo/OneDrive/Escritorio/Repo Programacion 1/programacion_1/CLASE_10/data_stark.json")
    lista_para_archivo = []
    while True:
        func.imprimir_menu()
        respuesta = func.validar_respuesta(input("Opción: "), '^[1-7]{1}$')
        if respuesta == "1":
            respuesta = input("\nCantidad de héroes a mostrar?: ")
            cantidad = int(func.validar_respuesta(respuesta, '^[1-9]{1,2}$'))
            cantidad = func.validar_len_lista(lista_heroes, cantidad)
            lista_para_archivo = lista_heroes[:cantidad].copy()
            func.mostrar(lista_para_archivo)
        elif respuesta == "2":
            respuesta = input('\nElegir Ascendente o Descendente ("asc" o "desc"): ')
            respuesta = func.validar_respuesta(respuesta, 'asc|desc')
            if respuesta == -1:
                print("Error! No es una elección válida")
            else:
                lista_para_archivo = func.ordenar_heroes(lista_heroes,"altura",respuesta)
                func.mostrar(lista_para_archivo, "altura")
        elif respuesta == "3":
            respuesta = input('\nElegir Ascendente o Descendente ("asc" o "desc"): ')
            respuesta = func.validar_respuesta(respuesta, 'asc|desc')
            if respuesta == -1:
                print("Error! No es una elección válida")
            else:
                lista_para_archivo = func.ordenar_heroes(lista_heroes,"fuerza",respuesta)
                func.mostrar(lista_para_archivo, "fuerza")
        elif respuesta == "4":
            respuesta_key = input('\nElegir tipo de key a calcular ("altura", "peso" o "fuerza"): ')
            respuesta_key = func.validar_respuesta(respuesta_key, 'altura|peso|fuerza')
            while respuesta_key == -1:
                print('\nIntente nuevamente:')
                respuesta_key = input('\nElegir tipo de key a calcular ("altura", "peso" o "fuerza"): ')
                respuesta_key = func.validar_respuesta(respuesta_key, 'altura|peso|fuerza')
            respuesta = input('\nElegir Menor o Mayor ("menor o mayor"): ')
            respuesta = func.validar_respuesta(respuesta, 'menor|mayor')
            while respuesta == -1:
                print('\nIntente nuevamente:')
                respuesta = input('\nElegir Menor o Mayor ("menor o mayor"): ')
                respuesta = func.validar_respuesta(respuesta, 'menor|mayor')
            lista_para_archivo = func.ordenar_promedio(lista_heroes, respuesta_key, respuesta)
            print(lista_para_archivo)
        elif respuesta == "5":
            print("")
        elif respuesta == "6":
            print("lista exportada")
            func.exportar_lista(lista_para_archivo)
        elif respuesta == "7":
            break
        else:
            print("Opción inválida, intente nuevamente")

heroes_app()

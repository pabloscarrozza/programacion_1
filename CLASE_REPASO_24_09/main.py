'''
1 - Listar TOP N videos
2 - Ordenar videos por duracion (UP/DOWN)
3 - Ordenar videos por cantidad de views (UP/DOWN)
4 - Buscar videos por título
5 - Exportar lista de videos a CSV
6 - Salir

        {
            "title": "Papa rosti con salchicha parrillera #paparosti #salchicha #patatas #papa #recetadepapa #shorts",
            "views": 11432,
            "length": 42,
            "img_url": "https://i.ytimg.com/vi/ZGni3XkUEeU/hqdefault.jpg",
            "url": "https://youtube.com/watch?v=ZGni3XkUEeU",
            "date": "2022-09-20 00:00:00"
        }
'''
import func

def paulina_app():
    # Construir una funcion que tome datos del json y lo transforma en una lista
    lista_videos = func.cargar_json("C:/Users/pablo/OneDrive/Escritorio/Repo Programacion 1/programacion_1/data_paulina.json")
    # Primero construir la mecanica
    # Armar un menu con un print primero para probar
    while True:
        print('''
        1 - Listar TOP N videos
        2 - Ordenar videos por duracion (UP/DOWN)
        3 - Ordenar videos por cantidad de views (UP/DOWN)
        4 - Buscar videos por título
        5 - Exportar lista de videos a CSV
        6 - Salir
        ''')
        respuesta = input()
        if respuesta == "1":
            top = int(input("\nCantidad de elementos a mostrar?: "))
            # VALIDAR QUE TOP SEA UN INT (CREAR FUNCION OBTENER ENTERO) con parámetros
            # VALIDAR QUE N NO SEA MAYOR A LA CANTIDAD DE LA LISTA
            func.mostrar(lista_videos[:top])
        elif respuesta == "2":
            print("Ordenar videos por duracion (UP/DOWN)")
        elif respuesta == "3":
            print("Ordenar videos por cantidad de views (UP/DOWN)")
        elif respuesta == "4":
            print("Buscar videos por título")
        elif respuesta == "5":
            print("Exportar lista de videos a CSV")
        elif respuesta == "6":
            print("Salir")
            break

paulina_app()

# Elegir un solo metodo de ordenamiento y aprenderlo


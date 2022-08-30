#   Pablo Scarrozza
'''Ejercicio Integrador 01

La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
'''
# Hacemos
# tipo_producto = ''
precio = 0
cantidad = 0
fabricante = ''

marca_barbijo_caro = ''
cantidad_barbijo_caro = 0
fabricante_barbijo_caro = ''
precio_barbijo_caro = 0

item_mas_unidades = 0
fabricante_mas_unidades = ''

cantidad_jabones = 0

for iteracion in range(2):

    tipo_producto = input("Ingrese tipo de producto(jabon, barbijo, alcohol): ")
    while tipo_producto != 'barbijo' and tipo_producto != 'jabon' and tipo_producto != 'alcohol':
        tipo_producto = input("Ingrese tipo de producto(jabon, barbijo, alcohol): ")
    
    # Version do-while utn
    while (True):
        precio = int(input("Ingrese el precio (entre $100 y $300): "))
        if precio >= 100 and precio <= 300:
            break

    while (True):
        cantidad = int(input("Ingrese la cantidad (menor que 1000): "))
        if cantidad > 0 and cantidad < 1000:
            break

    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")

#Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total.

    if tipo_producto == 'barbijo':
        if precio > precio_barbijo_caro:
            # Es mas caro que el anterior.
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
            marca_barbijo_caro = marca
    elif tipo_producto == 'jabon':
        cantidad_jabones += cantidad

    if cantidad > item_mas_unidades:
        item_mas_unidades = cantidad
        fabricante_mas_unidades = fabricante

print("Barbijo más caro hay: ", cantidad_barbijo_caro, " y lo fabrica: ", fabricante_barbijo_caro)
print("El item con más unidades lo fabrica: ", fabricante_mas_unidades)
print("Jabones hay: ", cantidad_jabones)
print("Fin del programa")


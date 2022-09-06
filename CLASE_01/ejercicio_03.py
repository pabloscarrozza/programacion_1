#   Pablo Scarrozza
'''Ejercicio Integrador 03

La división de alimentos de industrias Wayne está trabajando en un pequeño software 
para cargar datos de heroínas y héroes, para tener un control de las condiciones de 
heroes existentes, nos solicitan:
#!  1.  Nombre de Heroína/Héroe
#!  2.  EDAD (mayores a 18 años)
#!  3.  Sexo ("m", "f" o "nb")
#!  4.  Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
#?  A.  Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#?  B.  El sexo y nombre de Heroe | Heroína de mayor edad.
#?  C.  La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#?  D.  El promedio de edad entre Heroinas.
#?  E.  El promedio de edad entre Heroes de fuerza.
'''

continuar = 'si'
edad_menor_fuerza = 10000
edad_mayor = 0
contador_fuerza_f = 0
contador_magia_f = 0
suma_contador_f = 0
contador_heroinas = 0
acumulador_edad_f = 0
contador_fuerza_m = 0
acumulador_edad_fuerza_m = 0

while (continuar == 'si'):
    nombre = input('Ingrese el nombre de Heroína/Héroe: ')
    while (nombre.isnumeric()):
        nombre = input('ERROR! Ingrese el nombre de Heroína/Héroe: ')
    
    edad = int(input('Ingrese la edad (mayores a 18 años): '))
    while (edad < 18):
        edad = int(input('ERROR! Ingrese la edad (mayores a 18 años): '))

    sexo = input('Ingrese el sexo ("m", "f" o "nb"): ')
    while (sexo != 'm' and sexo != 'f' and sexo != 'nb'):
        sexo = input('ERROR! Ingrese el sexo ("m", "f" o "nb"): ')

    habilidad = input('Ingrese la habilidad ("fuerza", "magia", "inteligencia"): ')
    while (habilidad != 'fuerza' and habilidad != 'magia' and habilidad != 'inteligencia'):
        habilidad = input('ERROR! Ingrese la habilidad ("fuerza", "magia", "inteligencia"): ')

    if (habilidad == 'fuerza'):
        if (edad < edad_menor_fuerza):
            edad_menor_fuerza = edad
            nombre_menor_fuerza = nombre
        if (sexo == 'm'):
            contador_fuerza_m += 1
            acumulador_edad_fuerza_m += edad

    if (edad > edad_mayor):
        edad_mayor = edad
        nombre_mayor = nombre
        sexo_mayor = sexo

    if (sexo == 'f'):
        if (habilidad == 'fuerza'):
            contador_fuerza_f += 1
        elif (habilidad == 'magia'):
            contador_magia_f += 1
        contador_heroinas += 1
        acumulador_edad_f += edad

    continuar = input("Ingrese 'si' para continuar, 'no' para terminar: ")

print('El nombre del Héroe/Heroína de fuerza más joven es: ', nombre_menor_fuerza)

print('El nombre del Héroe/Heroína de mayor edad es: ', nombre_mayor, ' con ', edad_mayor, 'años de edad')

suma_contador_f = contador_fuerza_f + contador_magia_f

print('La cantidad de Heroinas que tienen habilidades de "fuerza" o "magia" es: ', suma_contador_f)

promedio_edad_f = acumulador_edad_f / contador_heroinas

print('El promedio de edad entre Heroinas es: ', promedio_edad_f)

promedio_edad_fuerza_m = acumulador_edad_fuerza_m / contador_fuerza_m

print('El promedio de edad entre Heroes de fuerza es: ', promedio_edad_fuerza_m)


#?  A.  Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#?  B.  El sexo y nombre de Heroe | Heroína de mayor edad.
#?  C.  La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#?  D.  El promedio de edad entre Heroinas.
#?  E.  El promedio de edad entre Heroes de fuerza.
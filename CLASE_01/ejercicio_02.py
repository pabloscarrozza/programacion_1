#   Pablo Scarrozza
'''Ejercicio Integrador 02

La división de alimentos está trabajando en un pequeño software para cargar las compras de 
ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#!  1.  PESO: (entre 10 y 100 kilos)
#!  2.  PRECIO POR KILO: (mayor a 0 [cero]).
#!  3.  TIPO VALIDAR: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el 
precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
#?  A.  El importe total a pagar, BRUTO sin descuento.
#?  B.  El importe total a pagar con descuento (Solo si corresponde).
#?  C.  Informar el tipo de alimento más caro.
#?  D.  El promedio de precio por kilo en total.
'''

continuar = 'si'
acumulador_kilos = 0
acumulador_precio_descuento = 0
importe_bruto = 0
precio_mas_caro = 0

while (continuar == 'si'):
    peso = input('Escriba el peso (entre 10 y 100 kilos): ')
    peso = int(peso)
    while (peso < 10 or peso > 100):
        peso = input('ERROR! Escriba un peso válido (entre 10 y 100 kilos): ')
        peso = int(peso)

    precio = input('Escriba el precio: ')
    precio = int(precio)
    while (precio < 0):
        precio = input('ERROR! Escriba un precio válido: ')
        precio = int(precio)

    tipo = input('Ingrese el tipo ("v", "a", "m"); (vegetal, animal, mezcla): ')
    while (tipo != 'v' and tipo != 'a' and tipo != 'm'):
        tipo = input('ERROR! Ingrese el tipo ("v", "a", "m"); (vegetal, animal, mezcla): ')
    
    acumulador_kilos += peso
    importe_bruto += peso * precio

    if(precio > precio_mas_caro):
        precio_mas_caro = precio
        tipo_mas_caro = tipo

    continuar = input("Ingrese 'si' para continuar, 'no' para terminar: ")


print('El importe total a pagar Bruto es: ', str(importe_bruto))

if (acumulador_kilos >= 100 and acumulador_kilos < 300):
    acumulador_precio_descuento = importe_bruto * 0.85
    print('El importe total con descuento (15%): ', str(acumulador_precio_descuento))
elif (acumulador_kilos >= 300):
    acumulador_precio_descuento = importe_bruto * 0.75
    print('El importe total con descuento (25%): ', str(acumulador_precio_descuento))

print('El tipo de alimento más caro es: ', str(tipo_mas_caro))

promedio = importe_bruto / acumulador_kilos

print('El promedio de precio por kilo en total es: ', promedio)

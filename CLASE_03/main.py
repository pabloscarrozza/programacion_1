from data import lista_bzrp
'''
parte de la lista para referencias

1 - Tema más visto
2 - Tema menos visto
3 - Tema más largo
4 - Tema más corto
5 - Duracion Promedio de temas
6 - Promedio de views
7 - Salir
'''

while True:
    respuesta = input("")

    if(respuesta == '7'):
        break



#print(lista_bzrp)  Para verificar si la lista existe
#print(lista_bzrp[0])  Trae el primer indice de la lista
#print(lista_bzrp[0]['title'])  Accedes a travez de la clave del diccionario
'''
views_maximo = lista_bzrp[0]['views']
video_maximo = lista_bzrp[0]
for video in lista_bzrp:
    if(video['views'] > views_maximo):
        views_maximo = video['views']
        video_maximo = video
'''
#!  Tema más visto
video_maximo = lista_bzrp[0]
for video in lista_bzrp:
    if(video['views'] > video_maximo['views']):
        video_maximo = video

print("Video: {0} - Vistas: {1}".format(video_maximo['title'],video_maximo['views']))

#!  Tema menos visto
video_minimo = lista_bzrp[0]
for video in lista_bzrp:
    if(video['views'] < video_minimo['views']):
        video_minimo = video

print("Video: {0} - Vistas: {1}".format(video_minimo['title'],video_minimo['views']))

#!  Tema más largo
video_length_maximo = lista_bzrp[0]
for video in lista_bzrp:
    if(video['length'] > video_length_maximo['length']):
        video_length_maximo = video

print("Video: {0} - Duración: {1}".format(video_length_maximo['title'],video_length_maximo['length']))

#!  Tema más corto
video_length_minimo = lista_bzrp[0]
for video in lista_bzrp:
    if(video['views'] < video_length_minimo['views']):
        video_length_minimo = video

print("Video: {0} - Duración: {1}".format(video_length_minimo['title'],video_length_minimo['length']))

#! Promedio de duración
acumulador_tiempo_videos = 0
for videos in lista_bzrp[0]:
    acumulador_tiempo_videos += video['length']


print("Promedio: {2} - QTY: {0} - Acumulador: {1} ".format(len(lista_bzrp),acumulador_tiempo_videos,acumulador_tiempo_videos/len(lista_bzrp)))

#! Promedio de vistas
acumulador_tiempo_vistas = 0
for videos in lista_bzrp[0]:
    acumulador_tiempo_vistas += video['views']


print("Promedio: {0:.2f} millones".format(acumulador_tiempo_vistas/len(lista_bzrp)/1000000))


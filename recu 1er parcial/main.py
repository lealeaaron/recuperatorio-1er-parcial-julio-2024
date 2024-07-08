from funciones import *


while True:
    respuesta = input("Menu\n"
                    "1- Cargar archivo .CSV\n"
                    "2- Mostrar ciclistas \n"
                    "3- Asignar tiempos \n"
                    "4- Mostrar ciclista mas rapido \n"
                    "5- Separar un tipo de bici\n"
                    "6-  \n"
                    "7-  \n"
                    "8-  \n"
                    "Ingrese una opcion:")
    
    if respuesta == "1":
        nombre_archivo = input("\nIngrese el nombre del archivo: ")
        datos = obtener_bicicletas(nombre_archivo)
    if respuesta == "2":
        mostrar_datos(datos)
    if respuesta == "3":
        asignar_tiempo(datos)
        mostrar_tiempos(datos,"tiempo")
    if respuesta == "4":
        el_mejor = mejor_ciclista(datos, "tiempo")
        mostrar_mas_rapido(el_mejor, "tiempo")
    if respuesta == "5":
        tipo = input("\ningrese el tipo a separar:")
        lista_tipo = filtrar_ciclistas(tipo, datos)
        mostrar_bicis(lista_tipo,"tipo")
        crear_archivo_bicis(lista_tipo,tipo)


    ### ej 9 : salir
    continuar = input("\ndesea continuar?: ")
    if continuar == "no":
        break
        
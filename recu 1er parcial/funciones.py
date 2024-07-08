import csv
import os


def get_path_actual(nombre_archivo):
    direccion_actual = os.path.dirname(__file__)
    return os.path.join(direccion_actual, nombre_archivo)

def obtener_bicicletas(nombre_archivo):
    with open(get_path_actual(nombre_archivo), "r", encoding = "utf-8") as archivo:
        lista = []
        archivo.readline().strip("\n").split(",")     
        for linea in archivo.readlines():
            bici = {}
            linea = linea.strip("\n").split(",")
            id, titulo, genero, rating = linea
            bici["id"] = int(id)
            bici["nombre"] = titulo
            bici["tipo"] = genero
            bici["tiempo"] = float(rating)
            lista.append(bici)
    return lista
    


######################### 2


def mostrar_datos(datos):
    tam = len(datos)
    print("                      ***Ciclistas***")
    print()
    print("|ID|           |nombre|                |tipo|        |tiempo|")
    print("-------------------------------------------------------------")
    for i in range(tam):
        mostrar_items(datos[i])
    print()


def mostrar_items(ciclista: list):
    print(f"{ciclista['id']:<3}    {ciclista['nombre']:<30}  {ciclista['tipo']:<14}  {ciclista['tiempo']:.2f}")



####################### 3

def asignar_tiempo(listado):
    from random import randint
    lista_con_tiempos = []
    for ciclista in listado:
        ciclista["tiempo"] = randint(50, 120)
        lista_con_tiempos.append(ciclista["tiempo"])
    return lista_con_tiempos
    

def mostrar_tiempos(lista, dato):
    print(f"id                               {dato}")
    for i in lista:
        print(f"{i['id']:<30}       {i[dato]} segundos")

####################### 4

def mejor_ciclista(lista, dato):
    ciclista_minimo = 0
    mejor_ciclista = None
    ciclista = True
    for i in lista:
        if ciclista or i[dato] < ciclista_minimo:
            ciclista_minimo = i[dato]
            mejor_ciclista = i
            ciclista = False
    return mejor_ciclista

def mostrar_mas_rapido(listado, dato):
    print(f"ciclista mas rapido")
    print(f"id: {listado['id']} | {dato}: {listado[dato]}")


############################## 5


def filtrar_ciclistas(dato, lista: list)-> list:
    lista_filtrada = []
    for ciclista in lista:  
        if ciclista["tipo"] == dato:
            lista_filtrada.append(ciclista)  # Agregar la película completa
    return lista_filtrada

def crear_archivo_bicis(lista, nombre_archivo):
    if not nombre_archivo.endswith('.csv'):
        nombre_archivo += '.csv'

    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        for elemento in lista:
            escritor.writerow([elemento])

    print(f"Archivo {nombre_archivo} creado exitosamente.\n")

def mostrar_bicis(lista, dato):
    print(f"nombre                               {dato}")
    for i in lista:
        print(f"{i['nombre']:<30}       {i[dato]}")


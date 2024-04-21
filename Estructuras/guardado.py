import json
import os


def guardar_lista(lista, nombre_archivo):
    ruta = os.path.join('../Guardados', nombre_archivo + '.json')
    with open(ruta, 'w') as f:
        json.dump(lista, f)


def cargar_lista(nombre_archivo):
    ruta = os.path.join('../Guardados', nombre_archivo + '.json')
    with open(ruta, 'r') as f:
        return json.load(f)



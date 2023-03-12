# Crea una funcion que al mandar como parametro un path me liste los elementos que contiene esa carpeta, 
# en caso sea una carpeta llamar otra vez tu funcion que lista los elementos de esa subcarpeta
# SANTOS EDUARDO MARTINEZ OCHOA
import os

def listar(path):
    elementos = os.listdir(path)

    for elemento in elementos:
        ruta = os.path.join(path, elemento)
        
        if os.path.isdir(ruta):
            print(f"Directorio: {ruta}")
            listar(ruta)
        else:
            print(f"Archivo: {ruta}")

listar(".")
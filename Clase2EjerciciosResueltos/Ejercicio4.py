# Definir una funcion que imprima los argumentos ingresados desde linea de comandos usando import sys.argv
# SANTOS EDUARDO MARTINEZ OCHOA
import sys

def imprimir_argumentos():
    argumentos = sys.argv[1:]
    print("Los argumentos ingresados son:")
    for argumento in argumentos:
        print(argumento)

imprimir_argumentos()

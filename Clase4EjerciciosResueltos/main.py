## Ejercicio2

import random

class Sorteo:
    def __init__(self, max_valor, cant_elementos):
        self.lista = []
        self.max_valor = max_valor
        self.cant_elementos = cant_elementos
    
    def sortear(self):
        for i in range(self.cant_elementos):
            self.lista.append(random.randint(1, self.max_valor))
    
    def mostrar(self):
        print(self.lista)
    
    def escoger_aleatorio(self):
        return random.choice(self.lista)

##############################################
import requests

def get_exchange_rate():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error al obtener los datos de la API. Código de error: {response.status_code}')

## Ejercicio4
from datetime import datetime

class Registro:
    def __init__(self, archivo):
        self.archivo = archivo
        with open(self.archivo, "w") as f:
            f.write("")

    def guardar_input(self, entrada):
        fecha_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        nombre_archivo = self.archivo.split('.')[0]
        with open(f"{nombre_archivo}_{fecha_actual}.txt", "a") as f:
            f.write(fecha_actual + "-" + nombre_archivo + "-" + entrada + "\n")

    def mostrar_registro(self):
        with open(self.archivo, "r") as f:
            contenido = f.read()
            print(contenido)

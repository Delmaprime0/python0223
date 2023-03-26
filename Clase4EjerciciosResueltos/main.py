## Ejercicio2

import random

class Sorteo:
    def __init__(self, Max_Valor, CantElements):
        self.list = []
        self.Max_Valor = Max_Valor
        self.CantElements = CantElements
    
    def sortear(self):
        for i in range(self.CantElements):
            self.list.append(random.randint(1, self.Max_Valor))
    
    def mostrar(self):
        print(self.list)
    
    def aleatorio(self):
        return random.choice(self.list)

##############################################


## Ejercicio4
from datetime import datetime

class Registro:
    def __init__(self, arch):
        self.arch = arch
        with open(self.arch, "w") as f:
            f.write("")

    def guardar(self, entrada):
        F_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        Name_Arch = self.arch.split('.')[0]
        with open(f"{Name_Arch}_{F_actual}.txt", "a") as f:
            f.write(F_actual + "-" + Name_Arch + "-" + entrada + "\n")

    def mostrar(self):
        with open(self.arch, "r") as f:
            contenido = f.read()
            print(contenido)
###########################################
import re

def ValidarNumCel(num):
    patron = r'^9\d{8}$'

    if not re.match(patron, num):
        return False
    if len(num) != 9:
        return False

    return True
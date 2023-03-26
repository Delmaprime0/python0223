## 2.	Crear una clase Sorteo, el cual inicializa una lista vacia de valores, el valor máximo que puede 
## tener un valor por agregar a la lista y la cantidad de elementos que se van a agregar a la lista, así 
## mismo un método de sortear números el cual serán agregadas a la lista con el máximo valor dado, un método 
## que muestre la lista de los valores sorteados y por ultimo un método que me permita escoger un valor 
## aleatorio de la lista. Use librería random

## Santos Eduardo Martinez Ochoa
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

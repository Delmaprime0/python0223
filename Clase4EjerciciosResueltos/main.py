## Santos Eduardo Martinez Ochoa

from Ejercicio2 import Sorteo
from Ejercicio3 import obtener
from Ejercicio4 import Registro
from Ejercicio5 import ValidarNumCel

sorteo = Sorteo(100, 10)
sorteo.sortear()
sorteo.mostrar()
print(sorteo.aleatorio())

##############################################

data = obtener()
if data:
    print(data)
else:
    print("Error")

###############################################

registro = Registro("mi_registro.txt")
texto = input("Digite el valor del txt: ")
registro.guardar(texto)

registro.mostrar()
###########################################

numero = input("Digite el valor del Numero: ")

if ValidarNumCel(numero):
    print('El número telefónico de celular es válido')
else:
    print('El número telefónico de celular no es válido')

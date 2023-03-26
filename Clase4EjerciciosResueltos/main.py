## Santos Eduardo Martinez Ochoa

from Ejercicio2 import Sorteo
from Ejercicio3 import obtener_tipo_cambio
from Ejercicio4 import Registro
from Ejercicio5 import ValidarNumCel

sorteo = Sorteo(100, 10)
sorteo.sortear()
sorteo.mostrar()
print(sorteo.aleatorio())

##############################################

data = obtener_tipo_cambio()
if data:
    print(data)
else:
    print("Error al obtener los datos del tipo de cambio.")

###############################################

registro = Registro("mi_registro.txt")

registro.guardar_input("Hola, mundo!")
registro.guardar_input("Esta es una prueba.")

registro.mostrar_registro()
###########################################

numero = input("Digite el valor del Numero: ")

if ValidarNumCel(numero):
    print('El número telefónico de celular es válido')
else:
    print('El número telefónico de celular no es válido')

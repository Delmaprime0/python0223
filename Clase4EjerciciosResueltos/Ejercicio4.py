
from main import Registro

registro = Registro("Registro.txt")

entrada1 = "Helloda"
entrada2 = "wenas"
entrada3 = "Practica"

registro.guardar(entrada1)
registro.guardar(entrada2)
registro.guardar(entrada3)

registro.mostrar()
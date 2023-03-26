
from main import Registro

registro = Registro("mi_registro.txt")

entrada_1 = "Helloda"
entrada_2 = "wenas"

registro.guardar_input(entrada_1)
registro.guardar_input(entrada_2)

registro.mostrar_registro()
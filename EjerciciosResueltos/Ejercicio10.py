# Defina un diccionario que tenga las siguientes llaves (nombre de curso, cantidad de alumnos, activo 
# ( tipo boleano), nombre de profesor, max nota, alumnos(lista)) a todos ellos como valor que lleven un valor de
# inicializacion, por ejemplo si es entero 0, si es string una cadena vacia.
# Realizar al menos 3 inputs para ingresar por teclado nuevos valores para el diccionario
# Imprimir diccionario
# Santos Eduardo Martinez Ochoa

diccionario = {"nombre del curso": "", "cantidad de alumnos": 0, "activo": False, "nombre de profesor": "", "max nota": 0, "alumnos": []}

diccionario["nombre de diccionario"] = input("Digite el nombre del diccionario: ")
diccionario["cantidad de alumnos"] = int(input("Digite la cantidad de alumnos: "))
diccionario["activo"] = bool(input("Digite si el diccionario está activo (True o False): "))
diccionario["nombre de profesor"] = input("Digite el nombre del profesor: ")
diccionario["max nota"] = float(input("Digite la nota máxima del diccionario: "))
diccionario["alumnos"] = input("Digite una lista de alumnos separados por comas: ").split(",")

print("El diccionario es:", diccionario)

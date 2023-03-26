import re

def validar_celular(numero):
    if re.match(r'^9\d{8}$', numero):
        return True
    else:
        return False

numero = "9876543231" # número inválido
if validar_celular(numero):
    print(f"{numero} es un número de celular válido.")
else:
    print(f"{numero} no es un número de celular válido.")
    
numero = "912345678" # número válido
if validar_celular(numero):
    print(f"{numero} es un número de celular válido.")
else:
    print(f"{numero} no es un número de celular válido.")
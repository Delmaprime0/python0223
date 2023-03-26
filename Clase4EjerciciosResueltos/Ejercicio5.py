## 5.	Realizar una función que valide que sea un numero telefónico de celular ingresado para eso la 
## expresión regular seria .r’^9\d*$’ (la cual significa que es un numero que inicia con 9) recordar que las 
## expresiones regulares son para strings y así mismo validar la longitud.

## Santos Eduardo Martinez Ochoa

import re

def ValidarNumCel(num):
    patron = r'^9\d{8}$'

    if not re.match(patron, num):
        return False
    if len(num) != 9:
        return False

    return True

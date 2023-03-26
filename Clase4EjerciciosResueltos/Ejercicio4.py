## 4.	Realizar una clase Registro que inicialice creando un archivo, un método que guarde el input(*)
## en un archivo de texto y uno que muestre todo el archivo.

## Santos Eduardo Martinez Ochoa

import datetime

class Registro:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "w") as f:
            f.write("")

    def guardar_input(self, input_data):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"{timestamp}-{self.filename}-{input_data}\n")

    def mostrar_registro(self):
        with open(self.filename, "r") as f:
            print(f.read())
# Realice un programa que imprima la ruta completa donde se encuentra trabajando
# Santos Eduardo Martinez Ochoa

import os
import sys

variable=sys.argv[0]
ruta_actual = os.path.dirname(os.path.abspath(variable))
print("La ruta del archivo actual es:", ruta_actual)
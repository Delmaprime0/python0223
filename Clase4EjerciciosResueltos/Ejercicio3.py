## 3.	Crear una función que se conecte a una api (https://api.apis.net.pe/v1/tipo-cambio-sunat)
## y mostrar datos devueltos y realizar una funcionalidad

## Santos Eduardo Martinez Ochoa

import requests

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
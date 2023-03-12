# Crear una funcion Main que valide el ingreso para un evento, dividir esta funcion main en al menos 3 sub-funciones
# SANTOS EDUARDO MARTINEZ OCHOA
def main():
    evento = obtener_evento()
    validar_evento(evento)
    procesar_evento(evento)

def obtener_evento():
    evento = input("Ingrese el nombre del evento: ")
    return evento

def validar_evento(evento):
    eventos_validos = ['fiesta', 'concierto', 'obra de teatro']
    if evento.lower() not in eventos_validos:
        raise ValueError("El evento ingresado no es válido.")

def procesar_evento(evento):
    print(f"Procesando el evento {evento}...")

main()
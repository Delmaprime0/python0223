# Crear una funcion Main que valide el ingreso para un evento, dividir esta funcion main en al menos 3 sub-funciones
# SANTOS EDUARDO MARTINEZ OCHOA
def main():
    evento = obtEvent()
    validar(evento)
    procesar(evento)

def obtEvent():
    evento = input("Digite el nombre del evento: ")
    return evento

def validar(evento):
    eventos_validos = ['fiesta', 'concierto', 'obra de teatro']
    if evento.lower() not in eventos_validos:
        raise ValueError("El evento digitado no es válido.")

def procesar(evento):
    print(f"Evento {evento}...")

main()
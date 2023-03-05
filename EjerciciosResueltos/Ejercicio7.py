# Realice un programa que lea 2 numeros por teclado y determine los siguientes aspectos
# Si los dos numeros son iguales
# Si los dos numeros son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero
# Santos Eduardo Martinez Ochoa
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 == num2:
    print("Los dos números son iguales")
else:
    print("Los dos números no son iguales")

if num1>num2:
    print("El primer numero es mayor que el segundo")
else:
    print("El segundo numero es mayor que el primero")

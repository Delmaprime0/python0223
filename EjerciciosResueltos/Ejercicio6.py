# Realice un programa que calcule la suma de los numeros hasta el valor ingresado
# Santos Eduardo Martinez Ochoa
Num = int(input("Digite el numero hasta el que quiere sumar: "))

suma = 0
for i in range(1, Num+1):
    suma += i

print("La suma de los numeros hasta ", Num, "es: ", suma)

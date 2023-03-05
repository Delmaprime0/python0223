# Calcule el area de un circulo, triangulo y cuadrado con radio ingresado desde el teclado
# Santos Eduardo Martinez Ochoa

from math import pi

opciones="""
    1) Calcule el area de un circulo
    2) Calcule el area de un triangulo
    3) Calcule el area de un cuadrado
    4) Hasta luego
"""
print(opciones)
opc=int(input("Digite la opcion a desarrollar:"))

if type(opc) == int:

    if opc==1:
        radio = float(input("Digite el valor del radio: "))
        area_circulo = pi * (radio ** 2)
        print("El area del círculo es:", area_circulo)

    elif opc==2:
        base = float(input("Digite el valor de la base del triangulo: "))
        altura = float(input("Digite el valor de la altura del triangulo: "))
        area_triangulo = (base * altura) / 2
        print("El area del triángulo es:", area_triangulo)

    elif opc==3:
        lado = float(input("Ingresa el valor del lado del cuadrado: "))
        area_cuadrado = lado ** 2
        print("El area del cuadrado es:", area_cuadrado)
    elif opc==4:
        print("Hasta Luego")
    else: 
        print("La opcion ingresada no es valida")
else:
    print("Por favor ingrese un numero entero valido")
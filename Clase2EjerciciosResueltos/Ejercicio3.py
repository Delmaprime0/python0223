# Definir una funcion que retorne el mayor valor al ingresar 2 numeros
# SANTOS EDUARDO MARTINEZ OCHOA
numero1 = input("Digite el primer numero: ")
numero2 = input("Digite el segundo numero: ")
def mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(mayor(numero1, numero2))  
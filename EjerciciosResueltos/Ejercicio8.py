# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
# contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide cono la guardada en la variable 
# sin tener en cuenta mayusculas y minusculas.
# Santos Eduardo Martinez Ochoa

contraseña = "contraseña"  
entrada = input("Digite la contraseña: ")  

if entrada.lower() == contraseña.lower():
    print("La contraseña ingresada es correcta")
else:
    print("La contraseña ingresada es incorrecta")

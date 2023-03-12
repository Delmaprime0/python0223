# Generar una funcion rango hasta un numero maximo con un step y agregar a una lista los numeros que cumplan las siguientes opciones, que se primos 
# SANTOS EDUARDO MARTINEZ OCHOA

def primes_in_range(start, end, step):
    primes = []
    for num in range(start, end+1, step):
        if num > 1:
            for i in range(2, int(num**(1/2))+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes
primes = primes_in_range(0, 10, 1)
print(primes)
# Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
# como un diccionario
# La biblioteca debera tener las siguientes operaciones.
# Obtener la lista de categorias de libros
# Obtener nombres de los libros y autores
# Poder cambiar el estado de un libro a prestado
# Lista de usuarios de la biblioteca
# SANTOS EDUARDO MARTINEZ OCHOA

biblioteca = {
    "categorias": ["aventuras", "ciencia ficción", "cuentos de hadas", "gótica" ],
    "libros": {
        "La vuelta al mundo en 80 dias": "Julio Verne",
        "1984": "George Orwell",
        "Caperucita Roja": "Charles Perrault",
        "Dracula": "Bram Stoker"
        
    },
    "prestamos": {},
    "usuarios": ["Pepe", "Jorge", "Martin", "Julio"]
}

print("Categorías de libros:")
for categoria in biblioteca["categorias"]:
    print(". " + categoria)

print("\nNombres de los libros y autores:")
for libro, autor in biblioteca["libros"].items():
    print(f"{libro} por {autor}")

# Cambiamos el estado de un libro a prestado
libro_prestado = "Caperucita Roja"
biblioteca["prestamos"][libro_prestado] = "Jorge"
print(f"\nSe ha prestado el libro {libro_prestado} a {biblioteca['prestamos'][libro_prestado]}.")

# Obtenemos la lista de usuarios de la biblioteca
print("\nUsuarios de la biblioteca:")
for usuario in biblioteca["usuarios"]:
    print("- " + usuario)
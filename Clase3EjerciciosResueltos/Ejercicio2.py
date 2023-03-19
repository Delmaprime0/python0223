# Santos Eduardo Martinez Ochoa

from main import Item
from main import Catalogo

catalogo = Catalogo()

product =Item("Llanta", "Llanta para automóvil", 1000)
catalogo.agregar_product(product)

product1 = Item("Batería", "Batería para automóvil", 2000)
catalogo.agregar_product(product1)

catalogo.mostrar_products()
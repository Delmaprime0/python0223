# Santos Eduardo Martinez Ochoa

from main import carCompra
from main import Producto

message="""
    1)Agregue producto
    2)Mostrar productos
    3)Quite producto
    4)Mostrar precio total
    5)Salir
"""
id=0
carrito=carCompra()
while True:

    print(message)
    opcion=int(input("Digite la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("Digite el nombre del producto:")
            precio=float(input("Digite el precio del producto:"))
            tipo=input("Digite el tipo del producto:")
            stock=int(input("Digite el stock del producto:"))
            release=int(input("Digite el release del producto:"))
            px=Producto(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print("Error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        id_producto = input("Digite el ID del producto a quitar: ")
        carrito.quitarProducto(id_producto)
    if opcion==4:
        carrito.calcularPrecio()
        print(f"El precio total es: {carrito.precioTotal}")
    if opcion==5:
        break
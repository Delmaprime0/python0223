# Santos Eduardo Martinez Ochoa
class Item:
    def __init__(self, name, descrip, prec):
        self.name = name
        self.descrip = descrip
        self.prec = prec
        
    def __str__(self):
        return f"{self.name}: {self.descrip} (${self.prec})"

class Catalogo:
    def __init__(self):
        self.products = []
    
    def agregar_product(self, product):
        self.products.append(product)
    
    def mostrar_products(self):
        for product in self.products:
            print(product)

##########################################################

def divicion(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("No dividas entre cero")
    else:
        return resultado

#########################################################

import os

class Product:
    def __init__(self, name, cod):
        self.name = name
        self.cod = cod
    
    def __str__(self):
        try:
            pais, lote, anio = self.cod.split("-")
        except ValueError:
            print("Error")
        else:
            print(f"Ruta: {os.getcwd()}")
            return f"Producto: {self.name}\nCodigo: {self.cod}\nPais de origen: {pais}\nNumero de lote: {lote}"
        finally:
            print("Fin")

##########################################################

class Producto:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} de tipo {self.tipo} con id: {self.id}  de costo {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
class carCompra:
    def __init__(self):
        self.listProduct=[]
        self.pTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listProduct.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProducto(self, id_producto):
        for producto in self.listProduct:
            if producto.id == int(id_producto):
                self.listProduct.remove(producto)
                producto.updateStock(producto.stock + 1)
                print("Producto eliminado del carrito.")
                break
        else:
            print("No se encontró el producto en el carrito.")

    def calcularPrecio(self):
        for i in self.listProduct:
            self.pTotal+=i.precio
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listProduct))
        if len(self.listProduct)>0:
            for i in self.listProduct:
                print(i)
        else:
            print("carrito vacio")

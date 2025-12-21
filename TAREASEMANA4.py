# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return f"{self.codigo} - {self.nombre} : ${self.precio:.2f}"


# Clase Carrito
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)
        print(f"✔ Producto agregado: {producto.nombre}")

    def total(self):
        return sum(producto.precio for producto in self.productos)

    def mostrar_carrito(self):
        print("\n🛒 Carrito de compras:")
        for producto in self.productos:
            print(producto.mostrar())
        print(f"💵 Total a pagar: ${self.total():.2f}")


# Clase Compra
class Compra:
    def __init__(self):
        self.carrito = Carrito()

    def realizar_compra(self, producto):
        self.carrito.agregar(producto)

    def pagar(self):
        print("\n✅ Compra realizada con éxito")
        self.carrito.mostrar_carrito()


# Ejecución del programa
producto1 = Producto(1, "Arroz", 1.50)
producto2 = Producto(2, "Leche", 0.90)
producto3 = Producto(3, "Pan", 0.50)

compra = Compra()

compra.realizar_compra(producto1)
compra.realizar_compra(producto2)
compra.realizar_compra(producto3)

compra.pagar()
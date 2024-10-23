from reto_16a_Modulos import Compra


class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


miprod = Producto("cartuchera", 3400, 6)

compra = Compra(miprod, 2, "20-4-50")

compra.mostrarFactura()

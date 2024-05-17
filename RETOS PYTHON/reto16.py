# Reto: Módulos
# Define una clase llamada Compra con los atributos de producto, cantidad y fecha actual de la compra.
# además crea un método para mostrar el total de la compra y un método para mostrar la factura. 

# Crea la clase Producto en un archivo diferente con los atributos de nombre, precio y cantidad disponible. 

# Importa la clase Compra e instancia un producto y utilízalo para instanciar una compra y generar una factura.


class Compra():
  def __init__(self, producto:str, cantidad:int,  fechaActual:str):
    self.producto = producto
    self.cantidad = cantidad
    self.fechaActual = fechaActual
  
  @property
  def mostrarTotal(self):
    return self.cantidad * self.producto.precio

  def mostrarFactura(self):
    total = self.mostrarTotal
    print(f"""
|------FACTURA------|
      {self.fechaActual}
Producto: {self.producto.nombre}
Precio: $1230
Stock: {self.cantidad} Unidades

-o-o-o-o-o-o-o-o-o-
        
Unidades compradas: 
Total: ${total}

|___________________|\n
""")

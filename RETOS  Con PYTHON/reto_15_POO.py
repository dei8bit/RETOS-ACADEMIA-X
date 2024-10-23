# Reto: POO
# Define una clase base llamada Empleado
# con los atributos de nombre, sueldo base, un método para calcular el sueldo actual y uno para mostrar los datos del empleado.
# Crea las clases Gerente y Programador
# que heredan de Empleado con métodos para:
# agregar un bono al sueldo
# agregar el lenguaje de programación que manejan, respectivamente . 🧠


class Empleado:
    def __init__(self, nombre: str, sueldoBase: float, antiguedad: int):
        self.nombre = nombre
        self.sueldoBase = sueldoBase
        self.antiguedad = antiguedad

    @property
    def sueldoActual(self):
        bonificacion = self.calcular_bonificacion()
        return self.sueldoBase + bonificacion

    def calcular_bonificacion(self):
        return self.antiguedad * self.bono_por_antiguedad

    @property
    def mostrarDatos(self):
        return f"Nombre: {self.nombre} - Sueldo: {self.sueldoActual}"


class Gerente(Empleado):
    def __init__(self, nombre: str, sueldoBase: float, antiguedad: int, bono: float):
        super().__init__(nombre, sueldoBase, antiguedad)
        self.bono_por_antiguedad = bono


class Programador(Empleado):
    def __init__(
        self,
        nombre: str,
        sueldoBase: float,
        antiguedad: int,
        bono: float,
        lenguajes: list,
    ):
        super().__init__(nombre, sueldoBase, antiguedad)
        self.bono_por_antiguedad = bono
        self.lenguajes = lenguajes

    @property
    def mostrarDatos(self):
        datos_empleado = super().mostrarDatos
        return f"{datos_empleado} - Habilidades: {', '.join(self.lenguajes)}"


# Ejemplo de uso
gerente1 = Gerente("Juan", 5000, 5, 1000)
programador1 = Programador("Pedro", 4000, 3, 800, ["Python", "JavaScript"])

print(gerente1.mostrarDatos)
print(programador1.mostrarDatos)

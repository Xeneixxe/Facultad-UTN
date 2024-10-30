class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f"Persona:[ Nombre:{self._nombre}, Edad:{self._edad}]"


class Empleado(Persona):  # Esta es la clase hija de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad, sueldo)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Sueldo:{self._sueldo}] {super().__str__}"


empleado1 = Empleado("Franco", 22, 7500)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

# Tarea: encapsular los atrubytos y agrear los metodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado("Marta", 25, 80000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = "Marilina"
empleado2.edad = 38
empleado2.sueldo = 70000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

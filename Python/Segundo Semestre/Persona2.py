class Persona2:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(
            f"Los datos a mostar son los siguientes: {self.nombre} {self.apellido} {self.edad}"
        )

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print("Estamos utilizando elmètodo get")
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):  # Mètodo Setter
        print("Estamos utilizando el mètodo set")
        self.nombre = nombre

    @property
    def apellido(self):
        return self.apellido

    @apellido.setter
    def apellido(self, apellido):
        self.apellido = apellido

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad

    def __del__(self):
        print(f"Persona2:{self.nombre}{self.apellido}{self.edad}")


if __name__ == "__main__":

    # @property
    # def telefono(self):
    #    return self.telefono

    # @telefono.setter
    # def telefono(self, telefono):
    #    self.telefono = telefono

    # @property
    # def direccion(self):
    #    return self.direccion

    # @direccion.setter
    # def direccion(self, direccion):
    #   self.direccion = direccion

    persona1 = Persona2("Franco", "Morales", "27")
    print(persona1.nombre)  # Llamamos al mètodo getter
    persona1.nombre = "Juan Carlo"  # Llamamos el mètodo setter
    print(persona1.nombre)  # Otra vez con el mètodo getter
    print(persona1.mostrar_detalles())  # Llamamos el mètodo mostrar detalles
    # Atributo read-only serua la edad porque no tiene el mètodo set
    print(persona1.edad)

    # Tare crear tres objetos màs utilizando los mètodos getter and setter
    # para  modificar, y mostrar los cambios con el metodo mostrar detalles
    persona2 = Persona2("Lionel", "Messi", "36")
    persona2.nombre = "Juan Roman"
    persona2.apellido = "Riquelme"
    persona2.edad = 48
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

persona3 = Persona2("Eva", "Vazquez", 50)
persona3.nombre = "Sergio"
persona3.apellido = "Morales"
persona3.edad = 60
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona3.mostrar_detalle())

persona3 = Persona2("Benjamin", "Morales", 21)
persona3.nombre = "Inti"
persona3.apellido = "Vallejos"
persona3.edad = 16
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
print(persona3.mostrar_detalle())
print(__name__)

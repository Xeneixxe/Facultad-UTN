class Vehiculo:
    """
    Definiruna clase padre llamada vehicule y dos clases hijas llamadas
    Auto y Bicicleta , los cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y métodos:

    Vehiculo(clase padre)
    -Atributos(color,  ruedas)
    -Métodos(__init__() y __str__())

    Crear un objeto de cada clase
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return "Color: " + self.color + ",Ruedas: " + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self) -> str:
        return super().__str__() + ", Velocidad(km/hr): " + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self) -> str:
        return super().__str__() + "Tipo: " + self.tipo


# Primer objeto de la clase padre Vehiculo

vehiculo = Vehiculo("Negro", 4)
print(vehiculo)

# Segundo objeto de la clase Auto

auto = Auto("Verde", 4, 180)
print(auto)


#Tercer objeto para la clase bicilcleta

bici=Bicicleta('Amarilla', 2, 'Playera')
print(bici)
class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.wkwargs = kwargs
        self._dni = dni

    def mostrar_detalle(self):  # self es igual a this
        print(
            f"La clase Personatiene los siguientes datos: {self.nombre}{self.apellido}{self._dni}{self.edad}, la direccion es: {self.args}, los datos importantes son: {self.wkwargs}"
        )


persona1 = Persona("Franco", "Morales", 22)  # Necesitamos enviar argumentos


print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


persona2 = Persona("Gabriel", "Casia", 16)
print(
    f"El objeto de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}"
)

print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)


persona1.nombre = "Lilina"
persona1.apellido = "Buccella"
persona1.edad = 40
print(
    f"El objeto1 modificado de la clase persona: {persona1.nombre}{persona1.apellido}. Su edad es: {persona1.edad}"
)

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento  qye vab a teer los objetos (acciones)

persona1.mostrar_detalle()  # la reerecnia en este caso se pasa de manera autoatica
persona2.mostrar_detalle()


# Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dará error

persona1.telefono = "12445234"
print(
    f"Este es el telefono de{persona1.nombre} {persona1.telefono}"
)  # Hemos creado un atrinuto de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo da error

persona3 = Persona(
    "Rogelio",
    "Romero",
    22,
    "Telefono",
    "261546456",
    "Calle Lopez",
    823,
    "Manzana",
    77,
    "Casa",
    18,
    Altura=1.83,
    Peso=105,
    CFavorito="Azul",
    Auto="Citroen",
    Modelo=2021,
)
persona3.mostrar_detalle()
persona4 = Persona(
    "Roscoldo",
    "Rumperto",
    15,
    "Telefono",
    "1274298323478",
    "Jaureche",
    175,
    "Manzana",
    15,
    "Casa",
    108,
    Altura=1.46,
    Peso=65,
    CFavorito="Negro",
    Auto="Wolswagen",
    Modelo=2010,
)

#print(persona1._dni)# Esto no se debe utilizr (esta encapsulado), esto dice que lo desconocemos python 


#persona3.__nombre# Esta totalmente encapsulado
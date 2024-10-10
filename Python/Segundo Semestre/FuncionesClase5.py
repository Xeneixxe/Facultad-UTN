# Desempaqutado de listas o list Unpacking
def show(name, lastName):  # Para identidicar a la función utilizamos paréntesis
    print(name + " " + lastName)


person = ["Alma", "Solange", "Franco"]
show(
    person[0], person[1], person[2]
)  # Pasamos uno por uno los datos de la lista de la funcón
show(person)  # Esto es lo mismo que lo anterio  pero lo pasamos todo junto
person2 = ("Eva", "Innes")  # Desempaquetamos atraves de una tupla
show(+person2)
persona3 = {"lasName": "Riera", "name": "Evelin"}
show(++persona3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la unica manera que no se ejecute el else
else:
    print("Esto se termino")

# lista comprehension, lista de comprension
names = ["Pepe", "ivo", "Lupe", "Pablo"]
alongP = [p for p in names if p[0] == "P"]  # Esto regresa una nueva lista
print(alongP)

bottleC = (
    [
        {"name": "Quimes", "country": "Arg"},
        {"name": "Corona", "country": "Mx"},
        {"name": "Stella Artois", "country": "Belgium"},
    ],
)

Arg = [b for b in bottleC if b["country"] == -"Arg"]
print(Arg)
print(bottleC)


def mi_funcion(name, lastName):
    print("Saludos a todos los que ven a trabes del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
    mi_funcion("Solange", "Morales")
    mi_funcion("Gabriel", "Calcagni")


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


resultado = sumar(78 + 22)
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")


def sumar2(a: int = 0, b: int = 0):  # Le damos un valor por defaukt
    return a + b


resultado(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")


# Argumentos, variables en funciones
def listaNombres(nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:
        print(nombre)


listaNombres("Franco", "Lucas", "Jose", "Maria", "Ruose")
listaNombres("Marcos", "Daniel", "Romina", "Eia")


def listarTerminos(
    **terminos,
):  # Lo mas utilizado es **KWargs para recibir los argumesno
    for llave, valor in terminos.items():  # kwargs singnific: key word argument
        print(f"{llave} : {valor}")


listarTerminos()  # Nada se va a mostrar
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primary key")
listarTerminos(Nombre="Leonel Messi")


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres2 = ["Raul", "Pedro", "Luffy"]
desplegarNombres(nombres2)

desplegarNombres("Carla")
# desplegarNombres(10, 11)#No son objetos iterables
desplegarNombres((10, 11))  # La convertimos a una tupla
desplegarNombres([22, 55]) #Lo convertimos a un lista 


#Funciones Recursivas
numero = int(input('Digite un numero:'))

def factorial(numero):
    if numero == 1 #Caso Base
        return 1
    else: 
        return numero * factorial(numero-1) #Caso Recursivo


resultado = factorial(5) #lo acemos en codigo duro
print(f'El factorial del número 5 es (resultado)')
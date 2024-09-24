# Lista= Ariel, Franco, tu hermana
# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ["Jose", "Gerardo", "Liliana", "Benja"]
# print(nombres)
# print(nombres[0])
# print(nombres[1])
# print(nombres[3])
# print(nombres[-1])
# print(nombres[-2])
print(nombres[0:2])  # Solo muestra el indice 0,1 pero no el indice 2
# Ir al inicio de la lista al indice (sin incluilo)
print(nombres[:3])
print(nombres[1:])
# Modificamos un valor
nombres[2] = "Lili"
nombres[0] = "Martin"
print(nombres)
# iterar una  lista
for nombre in nombres:  # Nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene la lista
print(len(nombres))  # le pasmos como parametro la lista

# Agregamos un elemento
nombres.append("Coco")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10, 45)
nombres.append([14, 5])
nombres.append(7)
print(nombres)


# Insertar un elemento en un indice especifico
nombres.insert(1, "Eva")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Coco")
print(nombres)


# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un elemento especifico
del nombres[2]
print(nombres)
# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))


# AAceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Accedera un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa",)  # Una tupla necesita aunque sea un elemento y la coma
# de lo contrario solo seria un sr cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:  # print esta usado \n para saltos de linea
    print(cocinar, end=" ")  # Usamos end= para elimiar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# del cocina Esto es para eliminar una tupla

# Tipo set
planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas))  # Usamos la funcion len = length significa largo

# Revisar si un elemento existe dentro de set
print("Marte" in planetas)


# Agregar un elemento
planetas.add("Tierra")  # add es una funcion
print(planetas)

# Eliminar elemento, puede arrojar un error si el elemento no exite
planetas.remove("Marte")
print(planetas)
planetas.discard("Tierra")
print(planetas)

# Limpiar nuestro set
planetas.clear()
print(planetas)


# Eliminar set
# del planetas
# print(planetas)

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)

diccionario = {
    "Ide": "Interated Development Enviroment",
    "POD": "Programacion Orientada a Objetos",
    "SABD": "Sistema de Administracion de Base de Datos",
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["Ide"])

# Otra forma de recuperar un elemento
print(diccionario.get("POD"))
print(diccionario.get("SABD"))


# Modificamos elementos
diccionario["Ide"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Recorrer los elementos
for termino in diccionario:  # Recorremos mostrando solos las llaves
    print(termino)

# Necesitamos una funccion para recorre un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)  # Muesta solo las laves

for valor in diccionario.values():  # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print("Ide" in diccionario)  # devuelve un booleano

# Agregar u elemento
diccionario["PK"] = "Primary key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("Ide")
print(diccionario)

# Vaciar un diccionario
diccionario.clear
print(diccionario)

# Eliminamos un diccionario
# del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2  # Concatenacion
print(lista3)

lista3.extend([7, 8, 9, 1])  # Funcion par agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) esto daria error por no ser el elemento parte de la lista
#
# #Como saber cuaos valores repetidos hay dentro de una lista
print(lista3.count(1))  # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.revese()
print(lista3)

# Para que una lista se multiplque repitiendo sus elementos
lista = lista3 * 2
print(lista)

# Metodo de ordenamiento en python ya es una funcion
lista3.sort()  # Ordena ascendentemente nuestra lista
print(lista3)
lista3.sort(reverse=True)  # Ordena descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (
    4,
    "Hola",
    6.79,
    [1, 2, 3],
    4,
    "Hola",
)  # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)  # Accion booleana, su respuestas es de tipo booleana
# Lo que podemos usar dentro de las tuplas son: index, cout, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de ser o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye"}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add(9)
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el 3 NO esta en el conjutno


# Como hacer la igualdad de dos conjuntos
print(conjunto2 == conjunto1)  # Nos da como respuesta un booleano

# Operaciones en conjuntos

conjunto3 = conjunto1 | conjunto2  # Lalinea une los dos conjuntos
print(conjunto3)


conjunto3 = conjunto1 & conjunto2  # que elemento tienen en comun
print(conjunto3)

conjunto3 = (
    conjunto1 - conjunto2
)  # Asigna el valor que esta en el conjunto 1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = (
    conjunto1 ^ conjunto2
)  # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(
    conjunto2.issubset(conjunto3)
)  # Aqui preguntamos si conjunto es un subcionjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))


print(
    conjunto3.issuperset(conjunto1)
)  # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(
    conjunto3.issuperset(conjunto2)
)  # Si es verdadero quiere decir que el conjunto 3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexxos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # No hay cosas en comun

# Conver un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hacer que el conjunto sera totalmente inmutable
# No se puede agreagar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {
    "Azul": "Blue",
    "Rojo": "Red",
    "Verde": "Green",
    "Amarillo": "Yellow",
}
print(diccionarioNuevo)
# Como eliminar
del diccionarioNuevo["Azul"]
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos dde datos
diccionario2 = {
    "Ariel": {"Edad": 40, "Altura": 1.83},
    "Osvaldo": [45, 185],
    "Natalia": [35, 1.67],
}

seleccionArgentina = {
    10: {
        "Nombre": "Leonel Messi",
        "Edad": 35,
        "Altura": 1.70,
        "Precio": "50 Millones",
        "Posicion": "Extremo Derecho",
    },
    11: {
        "Nombre": "Angel Di Maria",
        "Edad": 34,
        "Altura": 1.80,
        "Precio": "12 Millones",
        "Posicion": "Extremo Derecho",
    },
    21: {
        "Nombre": "Paulo Dybala",
        "Edad": 28,
        "Altura": 1.77,
        "Precio": "35 Millones",
        "Posicion": "Media Punta",
    },
    19: {
        "Nombre": "Nicolas Otamendi",
        "Edad": 34,
        "Altura": 1.83,
        "Precio": "3.5 Millones",
        "Posicion": "Defensa Central",
    },
    10: {
        "Nombre": "Franco Armani",
        "Edad": 35,
        "Altura": 1.89,
        "Precio": "3.5 Millones",
        "Posicion": "Arquero",
    },
    5: {
        "Nombre": "Leandro Paredes",
        "Edad": 30,
        "Altura": 1.82,
        "Precio": "8 Millones",
        "Posicion": "Medicampista central",
    },
    26: {
        "Nombre": "Nahuel Molina",
        "Edad": 26,
        "Altura": 1.75,
        "Precio": "28 Millones",
        "Posicion": "Lateral por derecha",
    },
    13: {
        "Nombre": "Cristian Romero",
        "Edad": 26,
        "Altura": 1.85,
        "Precio": "65 Millones",
        "Posicion": "Lateral por derecha",
    },
    20: {
        "Nombre": "Alexis Mac Allister",
        "Edad": 25,
        "Altura": 1.76,
        "Precio": "75 Millones",
        "Posicion": "Mediocampista",
    },
}

for llave in seleccionArgentina.items():
    print(llave, valor)


# Como tarea agregar 5 jugadores

# Pilas usando listas
pila = [1, 2, 3]

# Agregar  elementos a la pila por el final, siempre trabajamos con el ultimo elemetno
pila.append(4)
pila.append(5)
print(pila)


# Sacando elementos  por el final
elementoBorrado = pila.pop()  # Quita el elemento y lo guarda en la variable
print("Sacamos el elemento: {elementoBorrado}")
print("La pila ahora quedo asi: {pila}")

# Colas con listas
# Estructuras de datos de tipo fifo(First input/ first output)
cola = ["Ariel", "Osvalldo", "Liliana", "Pilar"]

# Agrupamos los elementos al final de la cola
cola.append("Natalia")
cola.append("Jose")
print(cola)


# Sacamos elementos de la cola
seRetira = cola.pop(0)
print("Atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print("Atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print("Atendido{seRetira}")
print(cola)

seRetira = cola.pop(0)
print("Atendido{seRetira}")
print(cola)

# Seguimos mostrando como recorre un diciionario con el ciclo for
for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")

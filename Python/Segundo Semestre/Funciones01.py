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

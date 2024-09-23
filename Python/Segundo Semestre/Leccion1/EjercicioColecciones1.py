# Ejercicio1: Eiminar duplicados de una lista
# Escriba un programa donde tenga una lista que a continuacion
# Eliminar los elementos repetidos, por ultimo mostrar la lista
lista = [3, 8, "Boca", "Banfield", 52, 23, 21, "Franco", 3, 8, 52, "Banfield"]
conjunnto = set(lista)  # Convertimos la lista a un conjunto de tipo set
# lista= list(conjunnto)#Converimos el conjunto a una lista
list = list(set(lista))  # La conversion hecha en una sola linde ade codigo (eficiente)
print(lista)

# Ejercicio 2: Operaciones de conjuntos con listas
# EScriba un programa que tenga 2 listas y que a continuacion
# Cree las siguientes litas (en las que no debe haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]


# Eliminar los elementos repetidos de ambas lista con conjunto
conjunto1 = set(lista1)
conjunto2 = set(lista2)


# Unir los conjuntos
juntar = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)
ambasListas = list(conjunto1 & conjunto2)

print("Lista de palabras que aparecen en las listas: {juntar}")

print(
    "Lista de palabras que aparecen en la primer lista, pero no en la segunda: {solo1}"
)
print(
    "Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}"
)
print("lista de palabras que aparecen en ambas listas: {ambasListas}")

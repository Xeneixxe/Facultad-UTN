import math  # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incuya los numeros menores a5
# Imprima por consola [1,3,2]


lista = []  # Definimos la lista
# Filtramos los elementos menores a 5 de la tabla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)


# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo"))
while numero < 0:
    print("Error --> Deberia se un número positivo")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")

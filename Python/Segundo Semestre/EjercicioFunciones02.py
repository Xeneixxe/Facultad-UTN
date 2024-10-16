# Ejercicio 2: Función con *args para multiplicar
# Creear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumetnos


# Definimos la función para multiplicar
def multiplicar_valores(*numeros):
    resultado = 1  # El cero no se puede multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado


# LLamamos a la función
print(multiplicar_valores(3, 5, 15))  # Le pasamos los argumentos

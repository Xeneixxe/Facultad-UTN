"""
#Sintaxis de range(inicio<opcional)>, fin <requerido>, incrmento <opcional>)




#Ejercicio 3: Crear un rango de 3  10 pero con un  incremento de 2 en 2, en lugar de 1 en 1 
#Ejemplo de Ejecucion: 3,5,7,9
"""

# Ejercicio 1: Iterar un rango de 0 a 1 e imprimir numeros divisibles entre 3
# Ejemplo de ejecucion: 0,3,56,9
print("Rango de 0 a 10 con numeros divisbles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 y imprimilos
# Ejemplo de ejecucion:2,3,4,5,6
print("Rango con valores de inico =2 y fin =6")
rango = range(2, 7)
for i in rango:
    print(i)


# Ejercicios 3: Crar un rango de 3 a 18 per con incrementos de 2 en 2 en lugar de 1 en 1
# Ejemplo de ejecucion: 3,5,7,9
print("Rango con valores de inicio = 3, fin =10, incremnto=2")
for i in range(3, 11, 2):
    print(i)

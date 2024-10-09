#Ejercicio  01: Crearuna función para sumar los valores recibidosde tipo
#númericos, utilizando argumentos variables *args como pararmetro de la 
#Funcion y agrear como resultado de la suma de todos los valores pasados 
#como argumentos 
#Definimos una función

def sumar_valor(**args)# Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

#LLamamos a la función 
print(sumar_valor(3, 5, 9, 2, 5))
# Ejercicio2: Adivina el numero
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio enre 1-100,y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N.#l proceso termina cuando el usuario acierta
# y alli se debe mostrar el número de intentos
import random

print("\t.: Juego Adivina el Número:.")
aleatorio = random.randint(
    0, 100
)  # Toma de 0 a  100 literal,  generamos un número aleatorio
contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif numero < aleatorio:
        print("\tNo es el número digite un número mayor")
    else:
        print(f"FELICITACIONES, acabas de adivinar el número{aleatorio}")
        break  # Rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")

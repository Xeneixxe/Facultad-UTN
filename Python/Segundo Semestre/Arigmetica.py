class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase en pthon
    vamos a hacer en esta clase algunas operaciones de:suma, resta, multipicación y más
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(7, 9)  # Lepasamos los argumentos para los operandos
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f"La resta de los números es: {aritmetica1.restar()}")
print(f"La multiplicación de los números es: {aritmetica1.multiplicar()}")
print(f"La división de los números es: {aritmetica1.dividir():.2f}")


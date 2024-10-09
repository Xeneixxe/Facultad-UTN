#Ejercicio 11: Agenda Telefonica 
#Hacer un programa que simule una agenda de contactos. Crear
#un diccionario donde la clave sea el nombre de usuario 
#y el valor sea el telefono, el programa tendrá el siguiete
#menú de opciones:
#   1. Nuevo contacto 
#   2. Buscar contacto
#   3. Ver contactos existentes
#   4. Salir 

agenda = {}

while True:
    print('\t.:MENÚ:.')
    print('\t1. Nuevo contacto ')
    print('\t2. Buscar contacto')
    print('\t3. Ver contactos existentes') 
    print('\t4. Salir ')
    opcion = int(input('Digite una opción de menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto:  ')
        telefono = input('Digite el número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Este contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre de contacto: ')
        if nombre in agenda:
            del(agenda(nombre))
            print('El contacto fue eliminado')
        else:
            print('El contacto no existe en su agenda')
    elif opcion == 3:
        print('Agenda de contactos ')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar la agenda de contactos')
        break
    else:
        print('Se equivoco de opción, digite nuevamente.')
    print()
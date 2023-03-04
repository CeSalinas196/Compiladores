'''
1.	Elabore una calculadora en Python que realice las operaciones de sumar, restar, multiplicar, dividir, calcule la raíz cuadrada. Considere las entradas de solo números (enteros y decimales sin el uso de “e”).

'''

import math

#función de suma para dos dígitos
def sumar(a, b):
    return a + b

#función de resta para dos dígitos
def restar(a, b):
    return a - b

#función de multiplicación para dos dígitos
def multiplicar(a, b):
    return a * b

#función de división para dos dígitos
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return a / b
    
#función de raiz cuadrada para un número
def raiz_cuadrada(a):
    if a < 0:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo"
    else:
        return math.sqrt(a)


#main
while True:
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular raíz cuadrada")
    print("0. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 0:
        break

    if opcion in [1, 2, 3, 4]:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado: ", sumar(a, b))
        elif opcion == 2:
            print("Resultado: ", restar(a, b))
        elif opcion == 3:
            print("Resultado: ", multiplicar(a, b))
        elif opcion == 4:
            print("Resultado: ", dividir(a, b))

    elif opcion == 5:
        a = float(input("Ingrese el número: "))
        print("Resultado: ", raiz_cuadrada(a))

    else:
        print("Opción inválida")
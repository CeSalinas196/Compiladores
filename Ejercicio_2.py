'''
2.	Elabore un convertidor de números donde se puede seleccionar la opción de entrada (binario, octal, decimal y hexadecimal) se ingrese el valor y después se seleccione una salida (binaria, octal, decimal o hexadecimal).

'''

#función de conversión de numeros
def convertir(numero, entrada, salida):
    """Convierte un número de un sistema numérico a otro"""
    if entrada == "binario":
        decimal = int(numero, 2)
    elif entrada == "octal":
        decimal = int(numero, 8)
    elif entrada == "decimal":
        decimal = int(numero)
    elif entrada == "hexadecimal":
        decimal = int(numero, 16)
    else:
        return "Error: sistema numérico de entrada no válido"

    if salida == "binario":
        resultado = bin(decimal)[2:]
    elif salida == "octal":
        resultado = oct(decimal)[2:]
    elif salida == "decimal":
        resultado = str(decimal)
    elif salida == "hexadecimal":
        resultado = hex(decimal)[2:]
    else:
        return "Error: sistema numérico de salida no válido"

    return resultado

#main
print("Convertidor de sistemas numéricos")

while True:
    entrada = input("Escriba el sistema numérico de Entrada:\n- binario\n- octal\n- decimal\n- hexadecimal\n")
    if entrada not in ["binario", "octal", "decimal", "hexadecimal"]:
        print("Sistema numérico no válido")
        continue

    salida = input("Escriba el sistema numérico de Salida:\n- binario\n- octal\n- decimal\n- hexadecimal\n")
    if salida not in ["binario", "octal", "decimal", "hexadecimal"]:
        print("Sistema numérico no válido")
        continue

    numero = input("Ingrese el número a convertir: ")

    resultado = convertir(numero, entrada, salida)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print("El número", numero, "en", entrada, "es igual a", resultado, "en", salida)

    continuar = input("¿Desea continuar? (s/n): ")
    if continuar.lower() != "s":
        break
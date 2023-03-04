'''

3.	Elabore un script donde se puede leer un archivo de texto y que identifique un patrón, cuando hay una secuencia de números (1 o más números), donde haya una secuencia de números y letras (1 o más números seguidos de 1 o más letras), un patrón donde identifique letras que contengan un más de tres vocales iguales (por ejemplo: palabra o aab3a; tienen 3 vocales a, emisión o oaaee solo tiene 2  vocales i emision, 2 vocales a, 2 vocales e; por lo cual no cumple la condición), y por último que identifique si hay un carácter especial en la entrada (por ejemplo ssdsdk&sd* donde se encontró & y *). Haga uso de la biblioteca de Python para identificar patrones.

'''

import re

patrones_encontrados = open('patrones_encontrados.txt', 'w', )
palabras_encontradas = []

try:
    file = open('texto_entrada.txt',"r")
    texto = file.read()  #Leer el archivo de texto
     
    #Patron de numeros y numero + letras
    patron_ltrs_numero = re.findall('\w*\d+\w*', texto)
    for x in patron_ltrs_numero:
        try:
            x=int(x)
            if type(x)==int:
                print(f'El patron es el numero: {x}')
                palabras_encontradas.append(x)
                patrones_encontrados.write(f'{x}\n')
        except Exception:
            print(f'Patron de Letras + numeros: {x}')
            palabras_encontradas.append(x)
    
    #Patron de vocales con > 3 vocales
    patron_vocales = re.compile(r"(([aeiou])\2\2)+", re.IGNORECASE)

    tests = texto.split()

    for y in tests:
        mt = [m.group(2) for m in patron_vocales.finditer(''.join(sorted(y)))]
        if len(mt):
            print(f"{y} tiene mas de 3 vocales  {mt}")
            palabras_encontradas.append(y)     

    #Patron de caracteres especiales
    patron_caracteres_especiales = re.compile(r"(([!*+#$,%&/()=?¡¿.]))+", re.IGNORECASE)
    
    for z in tests:
        mt = [m.group(2) for m in patron_caracteres_especiales.finditer(''.join(sorted(z)))]
        if len(mt):
            print(f"{z} tiene caracteres especiales: {mt}")
            palabras_encontradas.append(z) 

except FileNotFoundError: 
    print('No se encontraron archivos para leer')

#escribir en el archivo los patrones encontrados
for patron in palabras_encontradas:
    patrones_encontrados.write(f'{patron}\n')
    
#imprimir lista de palabras encontradas
print(palabras_encontradas)



"""
Existen dos reglas que identifican dos conjuntos de valores:

    a) El número es de un solo dígito.
    b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:

    esDeUnSoloDigito
    esImpar
    estaEnAmbos
    noEstaEnNinguno

el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto.
Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.
"""

import random

def main():
    
    un_digito = 0
    impares = 0
    esta_en_ambos = 0
    no_esta_en_ninguno = 0

    for contador in range(10):

        numero = random.randint(-50,50)
        print(numero)

        if -9 <= numero <= 9:
            un_digito += 1
            if numero % 2 != 0:
                impares += 1
                esta_en_ambos += 1
                
        else:
            if numero % 2 != 0:
                impares += 1
            elif numero % 2 == 0:
                no_esta_en_ninguno += 1

        
    print(f"La cantidad de numeros de un digito es: {un_digito}")
    print(f"La cantidad de numeros impares es: {impares}")
    print(f"La cantidad de numeros de al menos dos digitos y son impares es: {esta_en_ambos}")
    print(f"La cantidad de numeros de al menos dos digitos y no son impares es: {no_esta_en_ninguno}")
    

main()
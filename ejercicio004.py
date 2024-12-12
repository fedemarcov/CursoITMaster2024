"""

Escribir un programa que solicite al usuario ingresar tres numeros enteros.
El programa debe mostrar por pantalla el resultado de sumar los tres numeros de
la siguiente manera:
"[numero1] + [numero2] + [numero3] = [suma]"

"""


n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

suma = n1 + n2 + n3

print(f"{n1} + {n2} + {n3} = {suma}")
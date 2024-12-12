"""
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.
"""

def main():
    
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    
    if num1 == num2:
        print("Los numeros son iguales.")
    else:
        print("Los numeros son distintos.")

main()
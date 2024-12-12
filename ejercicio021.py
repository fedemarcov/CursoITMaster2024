"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.
"""

def main():
    
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"{num1} es menor que {num2}")
    else:
        print(f"Los numeros son iguales.")

main()
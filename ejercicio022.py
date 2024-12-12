"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

def main():
    
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))
    
    mayor = num1
    
    if num2 > num1:
        mayor = num2
        if num3 > num2:
            mayor = num3
        
    print(f"El numero mayor es {mayor}")

main()
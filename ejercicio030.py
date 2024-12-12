"""
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)
"""

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

es_divisible = num2 != 0 and num1 % num2 == 0
division = num1 / num2

if es_divisible:
    print(f"Es divisible. {num1} / {num2} = {division}")
else:
    print("No es divisible.")
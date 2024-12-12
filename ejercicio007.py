"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
a. Multiplicado por 10. (utilizar el operador *)
b. Dividido por 10. (utilizar el operador /)
c. Elevado al cuadrado. (utilizar el operador **)
Cada resultado debe mostrarse en una línea distinta.

Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""


def main():
    
    numero = int(input("Ingrese un numero: "))
    
    print(f"{numero} * 10 = {numero * 10}")
    print(f"{numero} / 10 = {numero / 10}")
    print(f"{numero} ** 2 = {numero ** 2}")



main()
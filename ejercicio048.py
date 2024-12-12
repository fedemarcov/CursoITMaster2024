"""
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación
a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar
el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada
sea ‘F’ nos indicará que no se desean calcular más operaciones.
"""


POSIBLES_OPERACIONES = ('+', '-', '*', '/', 'F')

def main():
    
    operacion = input("Ingrese una operacion ('+', '-', '*', '/', 'F'): ")
    
    while operacion != 'F':
        
        if operacion in POSIBLES_OPERACIONES:
        
            num1 = int(input("Numero 1: "))
            num2 = int(input("Numero 2: "))
            
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 > 0:
                    resultado = num1 / num2
                else:
                    resultado = "Error"
            
            print(f"{num1}{operacion}{num2} = {resultado}")
        else:
            print("Error en la operacion.")
    
        operacion = input("Ingrese una operacion ('+', '-', '*', '/', 'F'): ")


main()
"""
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla
las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecución:

    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0
"""
    

def main():
    
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    nota_3 = float(input("Nota 3: "))
    
    
    print(f"Notas: {nota_1}, {nota_2}, {nota_3}")
    print(f"Promedio: {(nota_1 + nota_2 + nota_3) / 3}")


main()    

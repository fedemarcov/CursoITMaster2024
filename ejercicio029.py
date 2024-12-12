"""
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno
e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre
0 y 10, debe informar un error.

    Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
    Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
    Se debe recuperar cuando al menos una de las dos notas es menor a 4.

"""


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))


notas_ok = 0 <= nota1 <= 10 and 0 <= nota2 <= 10

if notas_ok:
    if nota1 >= 7 and nota2 >= 7:
        print("Promocionaste!")
    elif nota1 >= 4 and nota2 >= 4:
        print("Aprobaste")
    else:
        print("Recupera")
else:
    print("Error en las notas")
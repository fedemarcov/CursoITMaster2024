"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre.
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando 
el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan
con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero - 'F' Femenino o 'M' Masculino:  ").upper()


edad_ok = edad >= 1 and edad <=120
genero_ok = genero in "MF"
nombre_ok = nombre != ""

datos_ok = edad_ok and genero_ok and nombre_ok

if datos_ok:
    if genero == 'F':
        if edad >= 60:
            cartel = f"Felicitaciones {nombre}, te jubilas!"
        else:
            cartel = f"Lo siento {nombre}, no tienes la edad para jubilarte."
    if genero == 'M':
        if edad >= 65:
            cartel = f"Felicitaciones {nombre}, te jubilas!"
        else:
            cartel = f"Lo siento {nombre}, no tienes la edad para jubilarte."
            
    print(cartel)
else:
    print("Error en los datos: ")
    if not edad_ok:
        print("Error en la edad.")
    if not genero_ok:
        print("Error en el genero.")
    if not nombre_ok:
        print("Error en el nombre.")


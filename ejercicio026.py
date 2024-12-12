"""
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon.
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
"""


from random import randint


cantidad_asientos = randint(1,30)
print(f"Disponibilidad de asientos aleatoria: {cantidad_asientos}")
cantidad_invitados = int(input("Ingrese la cantidad de invitados: "))

if cantidad_asientos >= cantidad_invitados:
    print("Tienes suficientes asientos para tus invitados.")
else:
    faltantes = cantidad_invitados - cantidad_asientos
    print(f"No hay asientos para todos los invitados. Faltan {faltantes} asientos.")



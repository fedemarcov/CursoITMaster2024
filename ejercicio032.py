"""
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad
de km que desea recorrer el usuario.
Tiene la siguiente tarifa:

    Viaje mínimo $50

    Si recorre entre 0 y 10km: $20/km

    Si recorre 10km o más: $15/km

Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario
y muestre el precio del viaje.
"""

viaje_minimo = 50
km_0a10 = 20
km_10omas = 15

valor_viaje = 0

kilometros = float(input("Kilometros recorridos: "))

if kilometros <= 10:
    valor_viaje = viaje_minimo + (kilometros * km_0a10)
    print(f"Valor viaje: ${valor_viaje}")
elif kilometros > 10:
    valor_viaje = viaje_minimo + (kilometros * km_10omas)
    print(f"Valor viaje: ${valor_viaje}")


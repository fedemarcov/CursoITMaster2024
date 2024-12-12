
"""
Leer un lista de numeros terminada en 0.

Mostrar la suma.
"""


def main():
    # ANTES
    sumador = 0
    contador = 0
    numero = int(input("Numero: "))
    while numero != 0:
        #DURANTE
        numero = int(input("Numero: "))
        sumador += numero
        contador += 1
    # Fin del While
    # DESPUES
    print(f"La suma total es: {sumador}")
    print(f"La cantidad de numeros sumados es: {contador}")



main()
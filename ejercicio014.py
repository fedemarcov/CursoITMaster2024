"""
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros,
junto con el valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor
total del terreno. Además, debe calcular la cantidad de metros de alambre necesarios para cercar
completamente el terreno a tres alturas distintas.
Pensando los pasos para resolver el problema:

Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable.
Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable.
Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra
variable. Calcular el valor total del terreno multiplicando el ancho por el largo y luego
multiplicando el resultado por el valor del metro cuadrado de tierra. Mostrar el valor total
del terreno al usuario. Calcular la cantidad de metros de alambre necesarios para cercar el 
terreno a tres alturas distintas. Por ejemplo, se puede calcular la cantidad de alambre necesaria
para cercar a 1 metro de altura, a 2 metros de altura y a 3 metros de altura. Para hacerlo, se
debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) y luego multiplicarlo
por la cantidad de alturas. Mostrar la cantidad de metros de alambre necesarios para cercar el 
terreno a las tres alturas distintas al usuario.
"""

def main():
    
    ancho_terreno = float(input("Ancho del terreno: "))
    largo_terreno = float(input("Largo del terreno: "))
    metros_cuadrados = ancho_terreno * largo_terreno
    valor_metro_cuadrado = float(input("Valor metro cuadrado: "))
    
    valor_terreno = (metros_cuadrados) * valor_metro_cuadrado
    
    metros_alambre = (ancho_terreno*2) + (largo_terreno*2)
    
    print(f"Dimensiones del terreno: {metros_cuadrados}m2")
    print(f"Valor del terreno: ${valor_terreno}")
    print(f"Perimetro 1 metro alambre: {metros_alambre}m")
    print(f"Perimetro 2 metros alambre: {metros_alambre*2}m")
    print(f"Perimetro 3 metro alambre: {metros_alambre*3}m")


main()
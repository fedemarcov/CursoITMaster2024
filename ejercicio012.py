"""
Escribir un programa en Python que solicite al usuario ingresar dos valores que
representen las medidas en grados de dos ángulos interiores de un triángulo. Luego,
calcular y mostrar por pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de
180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual 
a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la 
suma de los dos ángulos interiores ingresados al valor 180."
Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?

¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""

def main():
    
    angulo1 = int(input("Grados angulo 1: "))
    angulo2 = int(input("Grados angulo 2: "))
    angulo3 = 180 - angulo1 - angulo2
    
    print(f"El angulo 3 tiene {angulo3} grados.")



main()
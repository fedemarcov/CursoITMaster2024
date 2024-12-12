"""
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor
total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a
partir de esto calcular e informar lo requerido previamente.
"""

def main():
    
    persona1 = input("Nombre persona 1: ")
    inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))

    persona2 = input("Nombre persona 2: ")
    inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))

    persona3 = input("Nombre persona 3: ")
    inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))
    
    
    total = inversion_persona1 + inversion_persona2 + inversion_persona3
    
    
    porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
    porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
    porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2)
    
    
    print(f"La inversion de {persona1} es: {porcentaje_inversion_persona1}%")
    print(f"La inversion de {persona2} es: {porcentaje_inversion_persona2}%")
    print(f"La inversion de {persona3} es: {porcentaje_inversion_persona3}%")



main()
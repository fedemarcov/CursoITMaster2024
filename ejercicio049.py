"""
Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación 
de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe 
ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.
"""


POSIBLES_RESPUESTAS = ['S','N']

def main():
    
    respuesta = input(f"¿Desea continuar? {POSIBLES_RESPUESTAS}").upper()
    while respuesta not in POSIBLES_RESPUESTAS:
        print(f"Error: Ingrese {POSIBLES_RESPUESTAS}")
        respuesta = input(f"¿Desea continuar? {POSIBLES_RESPUESTAS}").upper()
    

main()
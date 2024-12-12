"""
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea
un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
"""

NOTA_MAXIMA = 10
NOTA_MINIMA = 0

def main():
    
    nota = int(input("Nota: "))
    
    while nota < NOTA_MINIMA or nota > NOTA_MAXIMA:         # MIENTRAS ERROR
        print(f"Error: Nota fuera de rango . . . [{NOTA_MINIMA} --- {NOTA_MAXIMA}] - Intentelo de nuevo.")
        nota = int(input("Nota: "))
        
    
    print(f"Nota correcta: {nota}")
        

main()


# OTRA FORMA DE HACERLO ES

es_nota_valida = False

while not es_nota_valida:
    nota = int(input("Ingrese una nota: "))
    
    if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        es_nota_valida = True
    else:
        print(f"Error: Nota fuera de rango . . . [{NOTA_MINIMA} --- {NOTA_MAXIMA}] - Intentelo de nuevo.")
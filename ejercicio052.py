"""
Escribir un programa que permita un programa que permita ingresar el nombre y la estatura (en metros con decimales) de cada jugador
de un equipo de baloncesto. La carga finalizará al indicarle al programa 'S' en la pregunta correspondiente. Calcular y mostrar la estatura promedio del equipo.

A) Calcular y mostrar la altura promedio del equipo
B) El nombre del jugador mas alto del equipo

"""


def main():
    
    contador_jugadores = 0
    sumador_estaturas = 0
    terminar_el_programa = False
    
    while not terminar_el_programa:
        
        nombre = input("Nombre: ")
        while nombre == "":
            print("Error en el nombre. Intentelo de nuevo.")
            nombre = input("Nombre: ")
            estatura_jugador = float(input("Estatura (en metros con decimales): "))
            # VALIDA LA ALTURA
            
            sumador_estaturas += estatura_jugador
            contador_jugadores += 1
            
        
    

main()
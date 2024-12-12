"""
Generar 10 numeros entre 1 y 10.
Mostrar cada numero generado.
Mostrar la suma.

"""


from random import randint

def main():
    
    suma = 0
    for x in range(10):
        numero = randint(1,10)
        print(numero)
        suma += numero
        
        
    print(f"La suma es: {suma}")
    
    
    
    
    
    
main()    
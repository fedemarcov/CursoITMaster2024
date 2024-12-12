"""
Ingresar 10 numeros
Mostrar la suma
"""

def main():
    
    cantidad = 10
    suma = 0
    
    while cantidad > 0:
        numero = int(input("Numero: "))
        suma += numero
        cantidad -= 1
    
    print(f"La suma total es: {suma}")

    
main ()    
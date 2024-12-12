"""
Escribir un programa que muestre todos los números enteros del 1 al 5,
y luego los mismos números pero en orden inverso.
"""

#  con WHILE

LINEA = "*"*25
def main():
    
    desde = 1
    hasta = 5
    
    print(f"{LINEA}\nDesde: {desde} hasta {hasta}\n{LINEA}")
    while(desde <= hasta):
        print(desde)   
        desde += 1
    
    
    desde = 1
    hasta = 5
    
    print(f"{LINEA}\nDesde: {hasta} hasta {desde}\n{LINEA}")    
    while(hasta >= desde):
        print(hasta)
        hasta -= 1
        
        
#con FOR

    desde = 1
    hasta = 5
    print(f"{LINEA}\nDesde: {desde} hasta {hasta}\n{LINEA}")
    
    for numero in range(desde,hasta+1):
        print(numero)
        
    
    desde = 1
    hasta = 5
    print(f"{LINEA}\nDesde: {hasta} hasta {desde}\n{LINEA}")
    
    for numero in range(hasta,desde-1,-1):
        print(numero)
    
    



main()
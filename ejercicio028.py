"""
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril").
Verificar que el mes sea válido e informar en caso que no lo sea.
"""

numero_mes = int(input("Numero de mes: "))

numero_mes_ok = 1 <= numero_mes <= 12
if numero_mes_ok:
    if numero_mes == 1:
        cartel = "Enero"
    elif numero_mes == 2:
        cartel = "Febrero"
    elif numero_mes == 3:
        cartel = "Marzo"
    elif numero_mes == 4:
        cartel = "Abril"
    elif numero_mes == 5:
        cartel = "Mayo"
    elif numero_mes == 6:
        cartel = "Junio"
    elif numero_mes == 7:
        cartel = "Julio"
    elif numero_mes == 8:
        cartel = "Agosto"
    elif numero_mes == 9:
        cartel = "Septiembre"
    elif numero_mes == 10:
        cartel = "Octubre"
    elif numero_mes == 11:
        cartel = "Noviembre"
    elif numero_mes == 12:
        cartel = "Diciembre"
else:
    cartel = "Error"
        
print(cartel)
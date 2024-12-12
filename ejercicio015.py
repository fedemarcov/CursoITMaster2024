"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base,
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas.
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde
en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor
total de las mismas.
¿Sobran datos? ¿Qué datos sobran?
"""

def main():
    
    nombre = input("Nombre: ")
    cantidad_ventas = int(input("Cantidad de ventas: "))
    valor_ventas = float(input("Valor de ventas: "))
    salario_base = 100000
    
    comision_fija_ventas = cantidad_ventas * 10000
    comision_valor_ventas = (valor_ventas * 5) / 100
    
    print(f"Este mes {nombre} realizo {cantidad_ventas} ventas por un valor total de {valor_ventas}")
    print(f"Salario basico: ${salario_base}")
    print(f"Comision fija por ventas: ${comision_fija_ventas}")
    print(f"Comision 5% valor ventas: ${comision_valor_ventas}")
    print(f"Salario mensual: ${salario_base+comision_fija_ventas+comision_valor_ventas}")


main()
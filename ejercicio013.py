"""
Escribir un programa para calcular el importe a cobrar por un vendedor,
considerando su sueldo fijo de $200000 pesos más el 16% del monto total de
ventas realizadas durante un mes.
Pensando los pasos para resolver el problema:

    1 Solicitar al usuario que ingrese el monto total de ventas realizadas por
    el vendedor durante el mes en una variable correspondiente.

    2 Calcular el 16% del monto total de ventas realizadas y almacenar el
    resultado en una variable.

    3 Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

    4 Mostrar el importe a cobrar por el vendedor.

Para pensar:

¿Qué pasaría si se modificara el sueldo fijo del vendedor?

Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para
calcular el salario total debería ser actualizada para reflejar el nuevo sueldo fijo.
En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría.
De igual manera, si el sueldo fijo disminuye, entonces el salario total también disminuiría.
Es importante actualizar la fórmula en el programa para asegurarse de que el cálculo del 
salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.

¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?
"""

def main():
    
    ventas_mes = float(input("Monto total de ventas en el mes: "))
    salario_basico = 200000
    comisiones = (ventas_mes * 16) / 100
    
    print(f"Salario basico: {salario_basico}")
    print(f"Comisiones(16%): {comisiones:.2f}")
    print(f"Total a cobrar: {salario_basico+comisiones:.2f}")


main()
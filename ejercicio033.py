"""
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

    - Menor de 5500.0 eldescuento es de l4.5%
    − Entre 5500.0 y 10000.0 el descuento es de l8%
    − Más de 10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""

DESCUENTO = 0

compra = float(input("Ingrese el valor de la compra: "))

if compra < 5500:
    DESCUENTO = 4.5
    A_DESCONTAR = (compra*DESCUENTO) / 100
    VALOR_TOTAL = compra - A_DESCONTAR
elif compra >= 5500:
    DESCUENTO = 8
    A_DESCONTAR = (compra*DESCUENTO) / 100
    VALOR_TOTAL = compra - A_DESCONTAR
elif compra > 10000:
    DESCUENTO = 10.5
    A_DESCONTAR = (compra*DESCUENTO) / 100
    VALOR_TOTAL = compra - A_DESCONTAR


print("=" * 30)
print("     Farmacia El Diegote")
print("=" * 30)
print(f"{'Valor de la compra:':<20} ${compra:>7.2f}")
print(f"{'Descuento (' + str(DESCUENTO) + '%):':<20} -${A_DESCONTAR:>7.2f}")
print("-" * 30)
print(f"{'Precio final:':<20} ${VALOR_TOTAL:>7.2f}")
print("=" * 30)


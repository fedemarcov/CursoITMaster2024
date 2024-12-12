"""
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo
básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto
por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario
bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

    Jubilación: 11%

    Obra Social: 3%

    Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil
(S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

    Jubilación - 999,99

    Obra Social - 999,99

    Sindicato - 999,99

Sueldo Neto 999,99
"""


sueldo_basico = float(input("Sueldo basico: "))
anos_antiguedad = int(input("Antiguedad: "))
estado_civil = input("Estado civil (S: Soltero / C: Casado): ").upper()

porcentaje_jubilacion = 0.11
porcentaje_obrasocial = 0.03
porcentaje_sindicato = 0.03

if estado_civil == "S":
    estado_civil = "Soltero"
    sueldo_bruto = sueldo_basico * (1 + 0.05 * anos_antiguedad)
    jubilacion = sueldo_bruto * porcentaje_jubilacion
    obra_social = sueldo_bruto * porcentaje_obrasocial
    sindicato = sueldo_bruto * porcentaje_sindicato
    sueldo_neto = sueldo_bruto - jubilacion - obra_social - sindicato
    
elif estado_civil == "C":
    estado_civil = "Casado"
    sueldo_bruto = sueldo_basico * (1 + 0.07 * anos_antiguedad)
    jubilacion = sueldo_bruto * porcentaje_jubilacion
    obra_social = sueldo_bruto * porcentaje_obrasocial
    sindicato = sueldo_bruto * porcentaje_sindicato
    sueldo_neto = sueldo_bruto - jubilacion - obra_social - sindicato
    
print("=" * 40)
print("            LIQUIDACIÓN DE SUELDO")
print("=" * 40)
print(f"Estado Civil: {estado_civil}")
print(f"Sueldo Básico: ${sueldo_basico:,.2f}")
print(f"Antigüedad: {anos_antiguedad} años")
print("-" * 40)
print("Descuentos:")
print(f"    Jubilación:      -${jubilacion:,.2f}")
print(f"    Obra Social:     -${obra_social:,.2f}")
print(f"    Sindicato:       -${sindicato:,.2f}")
print("-" * 40)
print(f"Sueldo Neto:        ${sueldo_neto:,.2f}")
print("=" * 40)
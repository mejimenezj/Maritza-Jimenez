def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado al monto total de la compra.

    Args:
    - monto_total: El monto total de la compra.
    - porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10%).

    Returns:
    - El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función desde el programa principal
monto_compra_1 = 1000
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

monto_compra_2 = 2000
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Resultados
print("Resultados de la primera llamada:")
print(f"Monto de la compra: ${monto_compra_1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")

print("\nResultados de la segunda llamada:")
print(f"Monto de la compra: ${monto_compra_2}")
print(f"Porcentaje de descuento: {porcentaje_descuento_2}%")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")
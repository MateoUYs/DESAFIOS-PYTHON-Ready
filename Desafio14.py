# Solicitamos la cantidad y la tasa de cambio
cantidad = float(input("Ingresa la cantidad en tu moneda local: "))
tasa_cambio = float(input("Ingresa la tasa de cambio (ej. 0.85 para USD a EUR): "))

# Realizamos la conversión
moneda_convertida = cantidad * tasa_cambio

# Mostramos el resultado
print(f"{cantidad} de tu moneda local equivale a {moneda_convertida:.2f} en la moneda objetivo.")
print(f"Conversión realizada el 22/10/2025 a las 11:40 AM.")
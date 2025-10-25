from datetime import datetime

# Solicitamos las dos fechas (formato AAAA-MM-DD)
fecha1_str = input("Ingresa la primera fecha (AAAA-MM-DD): ")
fecha2_str = input("Ingresa la segunda fecha (AAAA-MM-DD): ")

# Convertimos las cadenas a objetos datetime
fecha1 = datetime.strptime(fecha1_str, "%Y-%m-%d")
fecha2 = datetime.strptime(fecha2_str, "%Y-%m-%d")

# Calculamos la diferencia
diferencia = fecha2 - fecha1

# Mostramos el resultado
print(f"Diferencia al 22/10/2025, 12:02 PM: {diferencia.days} días")
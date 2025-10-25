# Solicitamos las calificaciones en una sola línea separadas por comas
calificaciones_str = input("Ingresa las calificaciones separadas por comas: ")

# Convertimos la cadena en una lista de números
calificaciones = [float(x.strip()) for x in calificaciones_str.split(',')]

# Calculamos el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Mostramos el resultado
print(f"\nPromedio de calificaciones al 22/10/2025, 11:44 AM: {promedio}")
# Inicializamos una lista para almacenar las calificaciones
calificaciones = []

# Solicitamos 5 calificaciones al usuario
for i in range(5):
    calif = float(input(f"Ingresa la calificación {i+1}: "))
    calificaciones.append(calif)

# Calculamos el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Mostramos el resultado
print(f"El promedio de las calificaciones es: {promedio}")
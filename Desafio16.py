# Solicitamos la cantidad de estudiantes
n = int(input("Ingresa la cantidad de estudiantes: "))

# Inicializamos contadores
aprobados = 0
desaprobados = 0

# Bucle para ingresar calificaciones
for i in range(n):
    calif = float(input(f"Ingresa la calificación del estudiante {i+1}: "))
    if calif >= 7:
        aprobados += 1
    else:
        desaprobados += 1

# Mostramos los resultados
print(f"\nResultados al 22/10/2025, 11:44 AM:")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes desaprobados: {desaprobados}")
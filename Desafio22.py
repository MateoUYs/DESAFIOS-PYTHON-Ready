# Solicitamos las notas separadas por comas
notas_str = input("Ingresa las notas separadas por comas: ")
notas = [float(x.strip()) for x in notas_str.split(',')]

# Calculamos el promedio
promedio = sum(notas) / len(notas)

# Mostramos el resultado
print(f"Promedio de las notas al 22/10/2025, 11:51 AM: {promedio}")

#Pregunta 2: Encuentra la nota más baja y la más alta. ¿Cómo lo harías?

# Encontramos la nota más baja y la más alta
nota_min = min(notas)
nota_max = max(notas)

# Mostramos los resultados
print(f"Nota más baja: {nota_min}")
print(f"Nota más alta: {nota_max}")

#Pregunta 3: Identifica la nota que más se repite. ¿Cómo lo harías?

from collections import Counter

# Contamos la frecuencia de cada nota
frecuencia = Counter(notas)
nota_mas_repetida = frecuencia.most_common(1)[0][0]

# Mostramos el resultado
print(f"Nota que más se repite: {nota_mas_repetida}")


from collections import Counter
import matplotlib.pyplot as plt

# Texto de ejemplo
texto = "hola mundo hola python mundo python codigo codigo hola"

# Dividimos el texto en palabras y contamos frecuencias
palabras = texto.split()
frecuencia = Counter(palabras)

# Obtenemos las 10 palabras más comunes
top_10 = frecuencia.most_common(10)

# Extraemos etiquetas y valores para el gráfico
etiquetas, valores = zip(*top_10)

# Creamos el gráfico de barras
plt.bar(etiquetas, valores, color=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'])
plt.title("Frecuencia de Palabras - 22/10/2025, 12:02 PM")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.show()

# Mostramos las estadísticas
print(f"Top 10 palabras más comunes al 22/10/2025, 12:02 PM: {top_10}")
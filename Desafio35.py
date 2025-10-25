def calcular_suma_promedio(lista):
    """
    Calcula la suma y el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números.
    
    Returns:
        tuple: Una tupla con (suma, promedio).
    """
    suma = sum(lista)
    promedio = suma / len(lista) if lista else 0  # Evita división por cero si la lista está vacía
    return (suma, promedio)

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
suma, prom = calcular_suma_promedio(numeros)
print(f"Suma al 22/10/2025, 12:15 PM: {suma}, Promedio: {prom}")

#Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.
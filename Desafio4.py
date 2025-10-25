# Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializamos un contador para los números pares
contador_pares = 0

# Recorremos la lista y contamos los números pares
for numero in numeros:
    if numero % 2 == 0:  # Si el número es divisible por 2, es par
        contador_pares += 1

# Mostramos el resultado
print(f"El número de elementos pares en la lista es: {contador_pares}")
# Solicitamos un número al usuario
numero = int(input("Ingresa un número: "))

# Verificamos si es múltiplo de cada número usando el operador %
es_multiplo_2 = (numero % 2 == 0)
es_multiplo_3 = (numero % 3 == 0)
es_multiplo_5 = (numero % 5 == 0)
es_multiplo_7 = (numero % 7 == 0)
es_multiplo_9 = (numero % 9 == 0)
es_multiplo_10 = (numero % 10 == 0)
es_multiplo_11 = (numero % 11 == 0)

# Mostramos los resultados El operador % calcula el residuo de la división. Si el residuo es 0, el número es múltiplo. Usamos una estructura condicional (if-else) para imprimir "Sí" o "No" según corresponda.
print(f"¿Es 30 múltiplo de 2? Sí" if es_multiplo_2 else f"¿Es 30 múltiplo de 2? No")
print(f"¿Es 30 múltiplo de 3? Sí" if es_multiplo_3 else f"¿Es 30 múltiplo de 3? No")
print(f"¿Es 30 múltiplo de 5? Sí" if es_multiplo_5 else f"¿Es 30 múltiplo de 5? No")
print(f"¿Es 30 múltiplo de 7? Sí" if es_multiplo_7 else f"¿Es 30 múltiplo de 7? No")
print(f"¿Es 30 múltiplo de 9? Sí" if es_multiplo_9 else f"¿Es 30 múltiplo de 9? No")
print(f"¿Es 30 múltiplo de 10? Sí" if es_multiplo_10 else f"¿Es 30 múltiplo de 10? No")
print(f"¿Es 30 múltiplo de 11? Sí" if es_multiplo_11 else f"¿Es 30 múltiplo de 11? No")
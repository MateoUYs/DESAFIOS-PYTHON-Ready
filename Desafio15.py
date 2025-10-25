# Solicitamos el texto al usuario
texto = input("Ingresa un texto: ")

# Contamos las palabras (dividiendo por espacios)
palabras = texto.split()
cantidad_palabras = len(palabras)

# Mostramos el resultado
print(f"El texto contiene {cantidad_palabras} palabra(s).")
print(f"Análisis realizado el 22/10/2025 a las 11:40 AM.")
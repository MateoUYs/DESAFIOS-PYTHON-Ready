import string

# Texto de ejemplo
texto = "  Hola, Mundo! 123  "

# Funciones del módulo string
texto_limpio = texto.strip()  # Elimina espacios al inicio y final
texto_mayus = texto.upper()   # Convierte a mayúsculas
texto_minus = texto.lower()   # Convierte a minúsculas

# Mostramos los resultados
print(f"Original al 22/10/2025, 12:02 PM: '{texto}'")
print(f"Con strip: '{texto_limpio}'")
print(f"Con upper: '{texto_mayus}'")
print(f"Con lower: '{texto_minus}'")
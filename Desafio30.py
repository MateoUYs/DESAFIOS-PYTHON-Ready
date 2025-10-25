import random
import string

# Caracteres disponibles
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generamos una contraseña de 8 caracteres
contraseña = ''.join(random.choice(caracteres) for _ in range(8))

# Mostramos el resultado
print(f"Contraseña generada al 22/10/2025, 12:02 PM: {contraseña}")
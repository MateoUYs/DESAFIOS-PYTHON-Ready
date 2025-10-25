import os

# Función para guardar texto en un archivo
def guardar_texto(texto, archivo):
    with open(archivo, 'w') as f:
        f.write(texto)
    print(f"Texto guardado en {archivo} al 22/10/2025, 12:02 PM.")

# Función para leer texto de un archivo
def leer_texto(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return f.read()
    else:
        return "Archivo no encontrado."

# Ejemplo de uso
texto = "Este es un texto de prueba."
guardar_texto(texto, "texto.txt")
contenido = leer_texto("texto.txt")
print(f"Contenido leído al 22/10/2025, 12:02 PM: {contenido}")
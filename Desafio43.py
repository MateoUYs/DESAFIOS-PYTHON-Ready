def invertir_oracion(oracion):
    """
    Invierte las palabras de una oración de forma recursiva sin usar funciones de inversión.
    
    Args:
        oracion (str): Oración a invertir.
    
    Returns:
        str: Oración con palabras invertidas.
    """
    # Dividimos en palabras y manejamos el caso base
    palabras = oracion.split()
    if len(palabras) <= 1:
        return oracion
    # Llamada recursiva invirtiendo las palabras
    return ' '.join([invertir_oracion(' '.join(palabras[1:]))] + [palabras[0]])

# Ejemplo de uso
texto = "hola mundo python"
resultado = invertir_oracion(texto)
print(f"Oración invertida al 24/10/2025, 11:45 PM: {resultado}")
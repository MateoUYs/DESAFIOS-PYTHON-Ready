def es_palindromo(cadena):
    """
    Verifica si una cadena es palíndromo (se lee igual al revés).
    
    Args:
        cadena (str): Cadena a verificar.
    
    Returns:
        bool: True si es palíndromo, False si no.
    """
    # Eliminamos espacios y convertimos a minúsculas
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Ejemplo de uso
texto = "radar"
resultado = es_palindromo(texto)
print(f"¿'{texto}' es palíndromo al 22/10/2025, 12:15 PM?: {resultado}")
#Crea una función llamada es_palindromo que tome una cadena y devuelva True si es palíndromo o False si no lo es.
#Compara la cadena con su reverso ([::-1]) después de limpiar espacios y convertir a minúsculas.
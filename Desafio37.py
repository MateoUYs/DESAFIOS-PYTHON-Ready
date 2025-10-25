def tienen_comun(lista1, lista2):
    """
    Verifica si dos listas tienen al menos un elemento en común.
    
    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.
    
    Returns:
        bool: True si hay un elemento en común, False si no.
    """
    return bool(set(lista1) & set(lista2))

# Ejemplo de uso
lista_a = [1, 2, 3]
lista_b = [3, 4, 5]
resultado = tienen_comun(lista_a, lista_b)
print(f"¿Tienen elementos en común al 22/10/2025, 12:15 PM?: {resultado}")

#Construye una función que tome dos listas y devuelva True si tienen al menos un elemento en común, de lo contrario, que devuelva False.
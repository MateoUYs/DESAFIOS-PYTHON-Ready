def buscar_palabra(texto, palabra, indice=0):
    """
    Busca recursivamente todas las ocurrencias de una palabra en un texto.
    
    Args:
        texto (str): Texto donde buscar.
        palabra (str): Palabra a buscar.
        indice (int): Índice inicial para la búsqueda recursiva.
    
    Returns:
        list: Lista de índices donde se encuentra la palabra.
    """
    ocurrencias = []
    posicion = texto.find(palabra, indice)
    if posicion == -1:  # No hay más ocurrencias
        return ocurrencias
    ocurrencias.append(posicion)
    ocurrencias.extend(buscar_palabra(texto, palabra, posicion + 1))
    return ocurrencias
import random

def contar_manzanas(total=0):
    """
    Simula recursivamente cómo un mono cuenta manzanas de forma distraída.
    
    Args:
        total (int): Total acumulado de manzanas contadas.
    
    Returns:
        int: Total final de manzanas contadas.
    """
    pila = random.randint(1, 5)  # El mono cuenta un número aleatorio de manzanas
    print(f"Contando {pila} manzanas...")
    for i in range(pila):
        total += 1
        print(f"Manzana {i+1} de la pila, total: {total}")
    print(f"¡Olvidé! Total acumulado: {total}")
    # Llamada recursiva hasta que decidamos parar (ej. max 10 manzanas)
    if total < 10:
        return contar_manzanas(total)
    return total

# Ejemplo de uso
resultado = contar_manzanas()
print(f"Total final de manzanas al 24/10/2025, 11:45 PM: {resultado}")
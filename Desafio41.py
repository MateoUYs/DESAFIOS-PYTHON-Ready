def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides recursivo.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
    
    Returns:
        int: MCD de a y b.
    """
    # Caso base: si b es 0, el MCD es a
    if b == 0:
        return abs(a)
    # Llamada recursiva con b y el residuo de a dividido por b
    return mcd(b, a % b)

# Ejemplo de uso
num1, num2 = 48, 18
resultado = mcd(num1, num2)
print(f"MCD de {num1} y {num2} al 24/10/2025, 11:45 PM: {resultado}")
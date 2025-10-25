def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
    
    Returns:
        int: MCD de a y b.
    """
    a, b = abs(a), abs(b)  # Usamos valores absolutos
    while b:
        a, b = b, a % b
    return a

# Ejemplo de uso
num1, num2 = 48, 18
resultado = mcd(num1, num2)
print(f"MCD de {num1} y {num2} al 22/10/2025, 12:15 PM: {resultado}")

#El Máximo Común Divisor (MCD) es un concepto matemático que ha sido estudiado desde tiempos antiguos. Atribuido a Euclides, el algoritmo para determinarlo es elegante y eficiente. Tu tarea es implementar una función que calcule el MCD de dos números utilizando el algoritmo de Euclides.
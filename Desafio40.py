def es_primo(n):
    """
    Verifica si un número es primo.
    
    Args:
        n (int): Número a verificar.
    
    Returns:
        bool: True si es primo, False si no.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(lista):
    """
    Cuenta la cantidad de números primos en una lista.
    
    Args:
        lista (list): Lista de números.
    
    Returns:
        int: Cantidad de números primos.
    """
    return sum(1 for num in lista if es_primo(num))

def main():
    """
    Función principal que integra y muestra los resultados de las funciones de primos.
    """
    # Lista de ejemplo
    numeros = [4, 7, 10, 13, 17, 20, 23]
    
    # Verificamos algunos números
    for num in [7, 10]:
        print(f"¿{num} es primo al 22/10/2025, 12:15 PM?: {es_primo(num)}")
    
    # Contamos primos en la lista
    cantidad = contar_primos(numeros)
    print(f"Cantidad de primos en {numeros} al 22/10/2025, 12:15 PM: {cantidad}")

# Ejecutamos el programa
if __name__ == "__main__":
    main()

#Crea dos funciones y un main que permita trabajar con números primos, un concepto matemático fundamental. En este desafío, deberás:

#Crear una función que verifique si un número es primo.
#Crear otra función que cuente la cantidad de números primos dentro de una lista dada.
#Implementar un main que integre estas funciones y muestre los resultados.

#es_primo() verifica divisibilidad hasta la raíz cuadrada del número.
#contar_primos() usa es_primo() para contar primos.
#main() integra las funciones y muestra resultados con documentación.
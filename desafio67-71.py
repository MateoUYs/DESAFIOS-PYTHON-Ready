# ======================
# Desafío 67
# ======================

def division():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos enteros.")
    else:
        print(f"Resultado de la división: {resultado}")
    finally:
        print("Operación finalizada.\n")

# division()  # Descomentar para probar


# ======================
# Desafío 68
# ======================

def operaciones_lista(valores):
    try:
        resultados = []
        for i in range(len(valores) - 1):
            resultados.append(valores[i] / valores[i + 1])
        print("Resultados:", resultados)
    except ZeroDivisionError:
        print("Error: División por cero detectada.")
    except TypeError:
        print("Error: Todos los elementos deben ser numéricos.")
    except ValueError:
        print("Error: Valor inválido.")
    finally:
        print("Fin del procesamiento de la lista.\n")

# operaciones_lista([10, 5, 0, 2])
# operaciones_lista([10, 'a', 5])


# ======================
# Desafío 69
# ======================

import math

def factorial(num):
    try:
        if not isinstance(num, int):
            raise TypeError("El número debe ser entero.")
        if num < 0:
            raise ValueError("El número no puede ser negativo.")
        if num > 1000:
            raise OverflowError("Número demasiado grande para procesar.")
        return math.factorial(num)
    except (TypeError, ValueError, OverflowError) as e:
        print("Error:", e)
    else:
        print(f"El factorial de {num} es {math.factorial(num)}")
    finally:
        print("Ejecución finalizada.\n")

# factorial(5)
# factorial(-2)
# factorial("hola")


# ======================
# Desafío 70
# ======================

class NegativeNumberError(Exception):
    """Excepción personalizada para números negativos."""
    pass

def raiz_cuadrada(num):
    try:
        if num < 0:
            raise NegativeNumberError("No se puede calcular la raíz cuadrada de un número negativo.")
        print(f"La raíz cuadrada de {num} es {math.sqrt(num):.2f}")
    except NegativeNumberError as e:
        print("Error:", e)
    except TypeError:
        print("Error: Debe ingresar un número válido.")
    finally:
        print("Fin del cálculo.\n")

# raiz_cuadrada(25)
# raiz_cuadrada(-9)


# ======================
# Desafío 71
# ======================

def leer_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        contenido = archivo.read()
        print("Contenido del archivo:\n", contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except PermissionError:
        print("Error: No tiene permiso para acceder al archivo.")
    else:
        print("\nArchivo leído correctamente.")
    finally:
        try:
            archivo.close()
            print("Archivo cerrado correctamente.")
        except NameError:
            print("El archivo no se abrió, nada que cerrar.\n")

# leer_archivo("texto.txt")
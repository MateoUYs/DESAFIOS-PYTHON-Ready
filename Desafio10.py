# Definimos las variables
a = int(input("Ingresa el dividendo (a): "))
b = int(input("Ingresa el divisor (b): "))

# Verificamos si b es cero
if b == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Calculamos el residuo usando el operador %
    residuo = a % b
    print(f"El residuo de la división de {a} entre {b} es: {residuo}")
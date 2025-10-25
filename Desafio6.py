# Solicitamos los tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Clasificamos en orden ascendente usando comparaciones encadenadas
if num1 <= num2 <= num3:
    print(f"Orden ascendente: {num1}, {num2}, {num3}")
elif num1 <= num3 <= num2:
    print(f"Orden ascendente: {num1}, {num3}, {num2}")
elif num2 <= num1 <= num3:
    print(f"Orden ascendente: {num2}, {num1}, {num3}")
elif num2 <= num3 <= num1:
    print(f"Orden ascendente: {num2}, {num3}, {num1}")
elif num3 <= num1 <= num2:
    print(f"Orden ascendente: {num3}, {num1}, {num2}")
else:
    print(f"Orden ascendente: {num3}, {num2}, {num1}")
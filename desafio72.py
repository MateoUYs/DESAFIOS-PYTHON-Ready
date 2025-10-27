num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 == num2 == num3:
    print("Todos los números son iguales:", num1)
elif num1 >= num2 and num1 >= num3:
    print("El mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor es:", num2)
else:
    print("El mayor es:", num3)

    codigos = [101, 202, 303, 404]
codigo_buscar = int(input("Ingrese el código de producto: "))
if codigo_buscar in codigos:
    print(f"El código {codigo_buscar} está en la posición {codigos.index(codigo_buscar)}")
else:
    print(f"El código {codigo_buscar} no se encontró")


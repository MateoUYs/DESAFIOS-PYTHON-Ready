# Solicitamos la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))

# Convertimos directamente a Fahrenheit y Kelvin
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Mostramos los resultados
print(f"{celsius}°C es igual a {fahrenheit}°F y {kelvin}K")
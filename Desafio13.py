# Lista para almacenar productos
productos = []

# Solicitamos detalles de los productos
while True:
    nombre = input("Ingresa el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    cantidad = int(input("Ingresa la cantidad: "))
    precio = float(input("Ingresa el precio unitario: "))
    productos.append((nombre, cantidad, precio))

# Calculamos y mostramos la factura
print("\n--- Factura ---")
print(f"Fecha: 22/10/2025, 11:40 AM")
print("Producto\tCantidad\tPrecio Unitario\tTotal")
total_factura = 0
for nombre, cantidad, precio in productos:
    total = cantidad * precio
    total_factura += total
    print(f"{nombre}\t\t{cantidad}\t\t{precio}\t\t{total}")
print(f"Total general: {total_factura}")
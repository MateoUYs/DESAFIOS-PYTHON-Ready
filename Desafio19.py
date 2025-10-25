#¿Cuántos tipos de productos hay en el inventario inicial?
# Inventario inicial
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

# Calculamos la cantidad de tipos de productos
cantidad_tipos = len(inventario)

# Mostramos el resultado
print(f"Cantidad de tipos de productos: {cantidad_tipos}")

#Pregunta 2: ¿Qué producto está en la tercera posición del inventario?
# Mostramos el producto en la tercera posición (índice 2)
print(f"Producto en la tercera posición: {inventario[2]}")

#Pregunta 3: ¿Cómo actualizarías el inventario después de la venta?
# Eliminamos "bananas" del inventario
inventario.remove("bananas")

# Mostramos el inventario actualizado
print(f"Inventario actualizado al 22/10/2025, 11:47 AM: {inventario}")

#Pregunta 4: ¿Cómo añadirías estos productos al inventario?
# Añadimos los nuevos productos al inventario
inventario.extend(["frutillas", "apio", "papas"])

# Mostramos el inventario actualizado
print(f"Inventario actualizado al 22/10/2025, 11:47 AM: {inventario}")

#Pregunta 5: ¿Cómo verificarías si las "papas" están en el inventario?
# Verificamos si "papas" está en el inventario
if "papas" in inventario:
    print(f"Sí, 'papas' está en el inventario al 22/10/2025, 11:47 AM.")
else:
    print("No, 'papas' no está en el inventario.")

#Pregunta 6: ¿Cómo decidirías qué producto sacar para hacer espacio para el "dragonfruit"?
# Verificamos si el inventario tiene más de 7 productos
if len(inventario) >= 7:
    # Eliminamos el último producto (ejemplo: el más antiguo o menos vendido)
    producto_eliminado = inventario.pop()
    print(f"Se eliminó {producto_eliminado} para hacer espacio.")
    inventario.append("dragonfruit")
else:
    inventario.append("dragonfruit")

# Mostramos el inventario actualizado
print(f"Inventario actualizado al 22/10/2025, 11:47 AM: {inventario}")

#Pregunta 7: ¿Cómo ordenarías el inventario?
# Ordenamos el inventario alfabéticamente
inventario.sort()

# Mostramos el inventario ordenado
print(f"Inventario ordenado al 22/10/2025, 11:47 AM: {inventario}")

#Pregunta 8: ¿Cómo proporcionarías una copia del inventario para que el nuevo empleado la use, asegurándote de que si el empleado hace cambios en su copia, el inventario original no se vea afectado?

# Creamos una copia del inventario
inventario_copia = inventario.copy()

# Mostramos la copia (el empleado puede modificar esta lista)
print(f"Copia del inventario para el empleado al 22/10/2025, 11:47 AM: {inventario_copia}")

# Ejemplo: Modificamos la copia (el original no cambia)
inventario_copia.append("naranja")
print(f"Copia modificada por el empleado: {inventario_copia}")
print(f"Inventario original sin cambios: {inventario}")
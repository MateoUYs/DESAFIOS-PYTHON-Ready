# TAD Producto
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

# TAD Tienda (contiene productos y empleados)
class Tienda:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.productos = []  # TAD Lista de Productos
        self.empleados = []  # TAD Lista de Empleados
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

# Cadena = Lista de Tiendas
cadena = []
tienda1 = Tienda(1, "Sucursal Centro")
tienda1.agregar_producto(Producto(101, "Laptop", 1000))
cadena.append(tienda1)
# TAD Libro
class Libro:
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        self.prestado_a = None  # Referencia al usuario

# TAD Usuario
class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []  # Referencias a libros

# TAD Préstamo (une entidades)
class Prestamo:
    def __init__(self, libro, usuario, fecha):
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha
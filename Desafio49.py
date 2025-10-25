# Desafio49.py
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = None

    def asignar_autor(self, autor):
        self.autor = autor
        autor.agregar_libro(self)

class Biblioteca:
    def __init__(self):
        self.autores = {}  # Diccionario: nombre -> Autor
        self.libros = {}   # Diccionario: isbn -> Libro

    def agregar_autor(self, autor):
        self.autores[autor.nombre] = autor

    def agregar_libro(self, libro, autor_nombre):
        if autor_nombre in self.autores:
            libro.asignar_autor(self.autores[autor_nombre])
            self.libros[libro.isbn] = libro

# Ejemplo de uso
bib = Biblioteca()
autor1 = Autor("Gabriel García Márquez")
bib.agregar_autor(autor1)
libro1 = Libro("Cien años de soledad", "Realismo mágico", "12345")
bib.agregar_libro(libro1, "Gabriel García Márquez")

# Modificamos Autor en Desafio49.py
class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def get_biografia(self):
        return f"{self.nombre} ({self.fecha_nacimiento}), {self.nacionalidad}"

    def lista_generos(self):
        return list(set(libro.genero for libro in self.libros))

# Ejemplo
autor1 = Autor("Gabriel García Márquez", "Colombiano", "1927-03-06")
print(autor1.get_biografia())  # Salida: Gabriel García Márquez (1927-03-06), Colombiano

# Agregamos a la clase Biblioteca en Desafio49.py
class Biblioteca:
    # ... (métodos anteriores)

    def buscar(self, isbn=None, autor_nombre=None):
        if isbn:
            return self.libros.get(isbn)
        if autor_nombre:
            return self.autores.get(autor_nombre)
        return None

# Ejemplo
bib = Biblioteca()
autor1 = Autor("Gabriel García Márquez", "Colombiano", "1927-03-06")
bib.agregar_autor(autor1)
libro1 = Libro("Cien años de soledad", "Realismo mágico", "12345")
bib.agregar_libro(libro1, "Gabriel García Márquez")

libro_encontrado = bib.buscar(isbn="12345")
autor_encontrado = bib.buscar(autor_nombre="Gabriel García Márquez")
print(libro_encontrado.titulo if libro_encontrado else "No encontrado")  # Cien años de soledad
print(autor_encontrado.nombre if autor_encontrado else "No encontrado")  # Gabriel García Márquez
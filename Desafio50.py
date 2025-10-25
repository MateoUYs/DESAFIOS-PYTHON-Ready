class Libro:
    def __init__(self, titulo, autor, isbn, genero=None):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = genero

    # Getters y Setters
    def get_titulo(self): return self.__titulo
    def set_titulo(self, titulo): self.__titulo = titulo
    def get_autor(self): return self.__autor
    def set_autor(self, autor): self.__autor = autor
    def get_isbn(self): return self.__isbn
    def set_isbn(self, isbn): self.__isbn = isbn
    def get_genero(self): return self.__genero
    def set_genero(self, genero): self.__genero = genero

    def asignar_autor(self, autor):
        self.__autor = autor
        autor.agregar_libro(self)

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento=None):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__fecha_nacimiento = fecha_nacimiento
        self.__libros = []

    # Getters y Setters con @property
    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, nombre): self.__nombre = nombre
    @property
    def nacionalidad(self): return self.__nacionalidad
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad): self.__nacionalidad = nacionalidad

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def get_biografia(self):
        return f"{self.__nombre} ({self.__fecha_nacimiento}), {self.__nacionalidad}"

    def lista_generos(self):
        return list(set(libro.get_genero() for libro in self.__libros if libro.get_genero()))

class Biblioteca:
    def __init__(self):
        self.__autores = {}  # Diccionario: nombre -> Autor
        self.__libros = {}   # Diccionario: isbn -> Libro

    def agregar_autor(self, autor):
        self.__autores[autor.nombre] = autor

    def agregar_libro(self, libro, autor_nombre):
        if autor_nombre in self.__autores:
            libro.asignar_autor(self.__autores[autor_nombre])
            self.__libros[libro.get_isbn()] = libro

    def buscar(self, isbn=None, autor_nombre=None):
        if isbn:
            return self.__libros.get(isbn)
        if autor_nombre:
            return self.__autores.get(autor_nombre)
        return None

# Funciones adicionales
def obtener_titulos(autor):
    return [libro.get_titulo() for libro in autor._Autor__libros]

def autor_mas_prolifico(autores):
    max_libros = -1
    autor_max = None
    for autor in autores:
        num_libros = len(autor._Autor__libros)
        if num_libros > max_libros:
            max_libros = num_libros
            autor_max = autor
    return autor_max

# Ejemplo de uso
if __name__ == "__main__":
    bib = Biblioteca()
    autor1 = Autor("Gabriel García Márquez", "Colombiano", "1927-03-06")
    bib.agregar_autor(autor1)
    libro1 = Libro("Cien años de soledad", autor1, "12345", "Realismo mágico")
    libro2 = Libro("El amor en los tiempos del cólera", autor1, "67890", "Realismo mágico")
    bib.agregar_libro(libro1, "Gabriel García Márquez")
    bib.agregar_libro(libro2, "Gabriel García Márquez")

    print("Títulos:", obtener_titulos(autor1))  # ['Cien años de soledad', 'El amor en los tiempos del cólera']
    print("Biografía:", autor1.get_biografia())  # Gabriel García Márquez (1927-03-06), Colombiano
    print("Géneros:", autor1.lista_generos())  # ['Realismo mágico']
    print("Autor más prolífico:", autor_mas_prolifico([autor1]).nombre)  # Gabriel García Márquez
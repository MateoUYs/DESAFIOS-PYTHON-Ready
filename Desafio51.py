class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.__tipo_poesia = tipo_poesia

    def get_tipo_poesia(self):
        return self.__tipo_poesia

class Usuario:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

class Bibliotecario(Usuario):
    def __init__(self, id, nombre, seccion, anos_experiencia):
        super().__init__(id, nombre)
        self.__seccion = seccion
        self.__anos_experiencia = anos_experiencia

    def get_seccion(self):
        return self.__seccion

    def get_anos_experiencia(self):
        return self.__anos_experiencia

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def mostrar_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor._Autor__nombre}, ISBN: {self.__isbn}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamano):
        super().__init__(titulo, autor, isbn)
        self.__formato = formato
        self.__tamano = tamano

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Formato: {self.__formato}, Tamaño: {self.__tamano}"

class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamano, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamano)
        self.__enlace_descarga = enlace_descarga

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Enlace: {self.__enlace_descarga}"

class Escritor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

class EscritorAcademico(Escritor):
    def __init__(self, nombre, nacionalidad):
        super().__init__(nombre, nacionalidad)
        self.__articulos = []

    def publicar_articulo(self, articulo):
        self.__articulos.append(articulo)
        return f"Publicado: {articulo}"

class Empleado:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

class Administrador:
    def gestionar(self):
        return "Gestionando recursos"

class Mantenimiento:
    def reparar(self):
        return "Reparando equipos"

class EmpleadoBiblioteca(Empleado, Administrador, Mantenimiento):
    def __init__(self, id, nombre, rol_adicional=None):
        super().__init__(id, nombre)
        self.__rol_adicional = rol_adicional

    def trabajar(self):
        tareas = [f"Trabajando como {self.__nombre}"]
        if isinstance(self.__rol_adicional, Administrador):
            tareas.append(self.gestionar())
        if isinstance(self.__rol_adicional, Mantenimiento):
            tareas.append(self.reparar())
        return "\n".join(tareas)

# Ejemplo de uso
if __name__ == "__main__":
    # Desafío 57
    poeta = Poeta("Pablo Neruda", "Chileno", "Amor y naturaleza")
    print(f"Poeta: {poeta._Autor__nombre}, Tipo de poesía: {poeta.get_tipo_poesia()}")

    # Desafío 58
    bibliotecario = Bibliotecario(1, "Ana", "Ficción", 5)
    print(f"Bibliotecario: {bibliotecario._Usuario__nombre}, Sección: {bibliotecario.get_seccion()}, Años: {bibliotecario.get_anos_experiencia()}")

    # Desafío 59
    autor = Autor("Gabriel García Márquez", "Colombiano")
    ebook = EBook("Cien años de soledad", autor, "12345", "PDF", "2MB", "http://descarga.com")
    print(f"Info EBook: {ebook.mostrar_info()}")

    # Desafío 60
    academico = EscritorAcademico("María Gómez", "Argentina")
    print(f"Artículo: {academico.publicar_articulo('Efectos de la IA')}")

    # Desafío 61
    empleado = EmpleadoBiblioteca(2, "Carlos", Administrador())
    print(empleado.trabajar())
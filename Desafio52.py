class Musico:
    def instrumento(self):
        return "Toca un instrumento genérico"

class Guitarista(Musico):
    def instrumento(self):
        return "Toca la guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "Toca la batería"

class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre

    def biografia(self):
        return f"Biografía de {self.__nombre}: Autor general"

class Escritor(Autor):
    def biografia(self):
        return f"Biografía de {self.__nombre}: Escritor de novelas"

class Libro:
    def __init__(self, titulo, autor, nivel):
        self.__titulo = titulo
        self.__autor = autor
        self.__nivel = nivel  # básico, intermedio, avanzado

    def mostrar_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor._Autor__nombre}, Nivel: {self.__nivel}"

class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, nivel, tema):
        super().__init__(titulo, autor, nivel)
        self.__tema = tema

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tema: {self.__tema}"

class Figura:
    def area(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    def area(self):
        return 3.1416 * self.__radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.__lado = lado

    def area(self):
        return self.__lado ** 2

class Operacion:
    def calcular(self, a, b):
        return 0

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

# Ejemplo de uso
if __name__ == "__main__":
    # Desafío 62
    musico1 = Guitarista()
    musico2 = Baterista()
    print("Guitarista:", musico1.instrumento())  # Toca la guitarra
    print("Baterista:", musico2.instrumento())   # Toca la batería

    # Desafío 63
    autor1 = Autor("Juan Pérez")
    escritor1 = Escritor("María Gómez")
    print(autor1.biografia())    # Biografía de Juan Pérez: Autor general
    print(escritor1.biografia()) # Biografía de María Gómez: Escritor de novelas

    # Desafío 64
    autor2 = Autor("Pedro López")
    libro1 = Libro("Matemáticas Básicas", autor2, "básico")
    libro_esp1 = LibroEspecializado("Física Avanzada", autor2, "avanzado", "Mecánica")
    print(libro1.mostrar_info())         # Título: Matemáticas Básicas, Autor: Pedro López, Nivel: básico
    print(libro_esp1.mostrar_info())     # Título: Física Avanzada, Autor: Pedro López, Nivel: avanzado, Tema: Mecánica

    # Desafío 65
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)
    print("Área Círculo:", circulo.area())    # Área Círculo: 78.54
    print("Área Cuadrado:", cuadrado.area())  # Área Cuadrado: 16

    # Desafío 66
    suma = Suma()
    mult = Multiplicacion()
    print("Suma (5, 3):", suma.calcular(5, 3))       # Suma (5, 3): 8
    print("Multiplicación (5, 3):", mult.calcular(5, 3))  # Multiplicación (5, 3): 15
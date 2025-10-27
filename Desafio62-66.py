# ======================
# Desafío 62
# ======================

class Musico:
    def instrumento(self):
        return "Toca un instrumento musical genérico."

class Guitarrista(Musico):
    def instrumento(self):
        return "Toca la guitarra eléctrica."

class Baterista(Musico):
    def instrumento(self):
        return "Toca la batería."

# Demostración de polimorfismo
musicos = [Guitarrista(), Baterista()]
for m in musicos:
    print(m.instrumento())


# ======================
# Desafío 63
# ======================

class Autor:
    def biografia(self):
        return "El autor es conocido por sus obras literarias."

class Escritor(Autor):
    def biografia(self):
        return "El escritor ha publicado varias novelas y ensayos."

# Instanciamos un escritor y mostramos el método sobrescrito
escritor = Escritor()
print(escritor.biografia())

# También podemos acceder al método original de la clase padre
print(super(Escritor, escritor).biografia())


# ======================
# Desafío 64
# ======================

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel = nivel

    def descripcion(self):
        return (f"'{self.titulo}' por {self.autor}. "
                f"Campo: {self.campo_estudio}, Nivel: {self.nivel}.")

# Instanciamos un LibroEspecializado
libro = LibroEspecializado("Introducción a la IA", "John Doe", "Inteligencia Artificial", "Avanzado")
print(libro.descripcion())


# ======================
# Desafío 65
# Polimorfismo en figuras geométricas
# ======================

import math

class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Polimorfismo
figuras = [Circulo(5), Cuadrado(4)]
for f in figuras:
    print(f"Área: {f.area():.2f}")


# ======================
# Desafío 66
# Polimorfismo en operaciones matemáticas
# ======================

class Operacion:
    def resultado(self, a, b):
        raise NotImplementedError("Debe sobrescribirse en la subclase.")

class Suma(Operacion):
    def resultado(self, a, b):
        return a + b

class Multiplicacion(Operacion):
    def resultado(self, a, b):
        return a * b

# Polimorfismo
operaciones = [Suma(), Multiplicacion()]
for op in operaciones:
    print(f"Resultado de {op.__class__.__name__}: {op.resultado(5, 3)}")

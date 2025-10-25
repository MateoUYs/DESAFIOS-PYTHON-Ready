# TAD base extensible
class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.habilidades = []  # Plugin system
    
    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

# Nueva habilidad = solo agregar al array, sin tocar TAD base
class Fuego:
    def usar(self): return "¡Llamas!"

guerrero = Personaje("Conan", 100)
guerrero.agregar_habilidad(Fuego())  # Fácil extensión
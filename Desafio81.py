class NodoABB:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar_abb(raiz, valor):
    if not raiz:
        return NodoABB(valor)
    if valor < raiz.valor:
        raiz.izquierdo = insertar_abb(raiz.izquierdo, valor)
    else:
        raiz.derecho = insertar_abb(raiz.derecho, valor)
    return raiz

def buscar_abb(raiz, valor):
    if not raiz or raiz.valor == valor:
        return raiz is not None
    if valor < raiz.valor:
        return buscar_abb(raiz.izquierdo, valor)
    return buscar_abb(raiz.derecho, valor)

# Construcción del ABB
valores = [5, 3, 7, 1, 4]
raiz = None
for valor in valores:
    raiz = insertar_abb(raiz, valor)

# Búsqueda
print("¿Existe 4?", buscar_abb(raiz, 4))  # Salida: True
print("¿Existe 6?", buscar_abb(raiz, 6))  # Salida: False
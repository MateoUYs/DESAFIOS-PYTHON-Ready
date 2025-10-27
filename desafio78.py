class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

# Construcción del árbol
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)

print("Recorrido en preorden:", end=" ")
preorden(raiz)  # Salida: 1 2 4 5 3 6
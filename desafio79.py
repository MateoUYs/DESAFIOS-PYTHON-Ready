class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def inorden_suma(nodo):
    if nodo:
        return inorden_suma(nodo.izquierdo) + nodo.valor + inorden_suma(nodo.derecho)
    return 0

raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)

suma = inorden_suma(raiz)
print("Suma en inorden:", suma)  # Salida: 21 (1+2+4+5+3+6)
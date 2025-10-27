class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def postorden_maximo(nodo):
    if not nodo:
        return float('-inf')
    max_izq = postorden_maximo(nodo.izquierdo)
    max_der = postorden_maximo(nodo.derecho)
    return max(nodo.valor, max_izq, max_der)

raiz = Nodo(1)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(2)
raiz.izquierdo.derecho = Nodo(6)

maximo = postorden_maximo(raiz)
print("Máximo en postorden:", maximo)  # Salida: 6
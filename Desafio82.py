class NodoExpresion:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol(expresion):
    def construir_nodo(tokens):
        if not tokens:
            return None
        token = tokens.pop(0)
        if token in ['+', '-', '*', '/']:
            nodo = NodoExpresion(token)
            nodo.izquierdo = construir_nodo(tokens)
            nodo.derecho = construir_nodo(tokens)
            return nodo
        return NodoExpresion(float(token))

    tokens = expresion.split()
    return construir_nodo(tokens)

def evaluar_arbol(nodo):
    if not isinstance(nodo.valor, str):
        return nodo.valor
    left = evaluar_arbol(nodo.izquierdo)
    right = evaluar_arbol(nodo.derecho)
    if nodo.valor == '+': return left + right
    if nodo.valor == '-': return left - right
    if nodo.valor == '*': return left * right
    if nodo.valor == '/': return left / right

# Ejemplo: "5 * 3 + 4"
arbol = construir_arbol("5 * 3 + 4".replace('*', '* ').replace('+', ' + ').split())
resultado = evaluar_arbol(arbol)
print("Resultado de 5 * 3 + 4:", resultado)  # Salida: 19.0 (5*3=15, 15+4=19)
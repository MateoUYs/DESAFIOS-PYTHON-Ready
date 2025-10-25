# Guardar este código en un archivo llamado 'formato_texto.py'
def negrita(texto):
    return f"**{texto}**"

def italica(texto):
    return f"_{texto}_"

# Programa principal
from formato_texto import negrita, italica

# Ejemplo de uso
texto = "Ejemplo"
print(f"Negrita al 22/10/2025, 12:02 PM: {negrita(texto)}")
print(f"Itálica al 22/10/2025, 12:02 PM: {italica(texto)}")
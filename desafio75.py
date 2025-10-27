lista1 = [1, 2, 3]
lista2 = [4, 5]
suma = [a + b if i < len(lista2) else a for i, a in enumerate(lista1)]
suma.extend([b + 0 for b in lista2[len(lista1):]] if len(lista2) > len(lista1) else [])
print("Suma:", suma)
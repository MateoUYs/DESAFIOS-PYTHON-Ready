# Definimos las matrices A y B
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Calculamos 2A
A_doble = [[2 * a for a in row] for row in A]

# Calculamos la transpuesta de B (B^T)
B_transpuesta = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]

# Sumamos 2A + B^T
resultado = [[A_doble[i][j] + B_transpuesta[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Mostramos el resultado
print(f"Matriz resultante (2A + B^T) al 22/10/2025, 11:57 AM: {resultado}")
#Explicación:

#   2A   multiplica cada elemento de    A    por 2.
#   B^T    intercambia filas por columnas de    B   .
#La suma se realiza elemento por elemento. Resultado esperado:
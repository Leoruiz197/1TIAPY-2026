def matriz_triangular_superior(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):  # Percorre apenas os elementos abaixo da diagonal principal
            if matriz[i][j] != 0:
                return False
    return True

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]
if matriz_triangular_superior(matriz):
    print("A matriz é triangular superior.")
else:
    print("A matriz não é triangular superior.")

def soma_linhas_colunas(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0]) if matriz else 0

    # Inicializa as listas de soma das linhas e colunas com zeros
    soma_linhas = [0] * num_linhas
    soma_colunas = [0] * num_colunas

    # Calcula a soma das linhas e das colunas
    for i in range(num_linhas):
        for j in range(num_colunas):
            soma_linhas[i] += matriz[i][j]
            soma_colunas[j] += matriz[i][j]

    return soma_linhas, soma_colunas

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_linhas, soma_colunas = soma_linhas_colunas(matriz)
print("Soma das linhas:", soma_linhas)
print("Soma das colunas:", soma_colunas)

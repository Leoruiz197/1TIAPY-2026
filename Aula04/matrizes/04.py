def trocar_linhas(matriz, linha1, linha2):
    matriz[linha1], matriz[linha2] = matriz[linha2], matriz[linha1]

# Exemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trocar_linhas(matriz, 0, 1)

# Mostrar a matriz após a troca
for linha in matriz:
    print(linha)

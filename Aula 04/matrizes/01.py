def matriz_zeros_uns(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

# Exemplo de uso
n = 5
matriz = matriz_zeros_uns(n)
for linha in matriz:
    print(linha)

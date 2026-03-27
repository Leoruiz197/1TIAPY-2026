matriz = [
    ['a','b'],
    ['c','d'],
    ['e','f']
]

transposta = []

for j in range(len(matriz[0])):
    nova_linha = []
    for i in range(len(matriz)):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)
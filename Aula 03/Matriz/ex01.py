matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matriz2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j] + matriz2[i][j], end = " ")
    print()
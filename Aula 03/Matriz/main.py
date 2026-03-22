matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

nova_linha = [10, 11, 12]
matriz.append(nova_linha)

print(matriz[3][0])

matriz[1].insert(0,100)

del matriz[2]

elemento = matriz[0].pop(2)
print(f"O elemento {elemento} foi removido da lista!")

for linha in matriz:
    print(linha)

matriz2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for linha in matriz2:
    for elemento in linha:
        print(elemento, end = " ")
    print()
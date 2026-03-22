num = int(input("Digite um numero para multiplicar a matriz: "))

matriz = [
    [1,2],
    [3,4]
]

for linha in matriz:
    for elemento in linha:
        print(elemento * num, end = " ")
    print()
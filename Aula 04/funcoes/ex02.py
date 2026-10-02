# Maior de Três:
# Crie uma função que recebe três
# números e retorna o maior deles.

def maiordeTres(n1,n2,n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    elif n2 > n3:
        return n2
    else:
        return n3

lista = []
for i in range(3):
    lista.append(int(input(f" Digite o {i+1}° numero: ")))

print(f"O maior numero da sequencia é: {maiordeTres(lista[0],lista[1],lista[2])}")


# listaitens = [4,7,23,6,3]
# maior = 0

# for i in range(len(listaitens)):
#     if listaitens[i] > maior:
#         maior = listaitens[i]

# print(maior)
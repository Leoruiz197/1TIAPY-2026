numeros = [3,7,4,2,8,3,43,1,54,76]
numeros2 = [1,2,3]

numeros.append(10)
print(numeros)

numeros.extend(numeros2)
print(numeros)

numeros.insert(5,51) #insert serve para...
print(numeros)

numeros.remove(3)
print(numeros)

num = numeros.pop(0)
print(f"O numero no index 0: {num}, foi removido com sucesso!")
print(numeros)

print(numeros2)
numeros2.clear()
print(numeros2)

index = numeros.index(43)
print(f"O numero 43 procurado, se encontra no index: {index}")
print()
contagem = numeros.count(3)
print(f"\nO numero 3 aparece {contagem} vezes na lista")

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)


novoNumeros = numeros.copy()
print(numeros)
novoNumeros.clear()
print(novoNumeros)
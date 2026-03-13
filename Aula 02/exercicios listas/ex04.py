nomes = ["Pedro","Cleusa","Zé","Rian","Kevin"]

nome = input("Digite um nome: ")
contagem = nomes.count(nome)

if contagem > 0:
    print(f"O nome: {nome}, está presente na lista, {contagem} vez(es)")
else:
    print(f"Nao foi localizado {nome} na lista")


if nome in nomes:
    print(f"O nome: {nome}, está presente na lista")
else:
    print(f"Nao foi localizado {nome} na lista")
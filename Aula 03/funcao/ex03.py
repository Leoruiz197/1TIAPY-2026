lista = []

def mediaLista(lista):
    return sum(lista) / len(lista)
    


while True:
    nota = float(input("Digite a nota ser inserida na lista (-1 para sair): "))
    if nota < 0:
        break
    lista.append(nota)
    print(f"A nota {nota}, foi inserida com sucesso!")

print(f"A média da lista:{lista} com {len(lista)} elementos, é: {mediaLista(lista):.2f}")
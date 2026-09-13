lista = [1, 2, 3, 4, 5]

try:
    num = int(input("Digite um número: "))
    if(num < 0 or num >= len(lista)):
        raise IndexError("Índice fora dos limites da lista.")
    print(f" o elemento {num} é {lista[num]}")

except IndexError:
    print("Índice fora dos limites da lista.")

except ValueError:
    print("Valor inválido. Por favor, digite um número inteiro.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
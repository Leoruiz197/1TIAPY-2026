try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você inseriu o número {numero}.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

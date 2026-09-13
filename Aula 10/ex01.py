try:
    num = int(input("Digite um numero inteiro: "))
    print(f"O numero digitado é: {num}")

except ValueError:
    print("Por favor, digite um numero inteiro valido.")
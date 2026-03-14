num = int(input("Digite um numero par: "))

while num % 2 != 0:
    num = int(input("Errado, digite novamente um numero par: "))

print(f"O numero digitado: {num} é par!")
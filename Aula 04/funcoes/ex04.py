# Fatorial: Crie uma função que recebe um número
# retorna o seu fatorial.

def fatorial(n):
    for i in range(1,n)[::-1]:
        n *= i

    return n

num = int(input("Digite um numero para saber seu fatorial: "))
print(f"O fatorial de {num} é {fatorial(num)}")
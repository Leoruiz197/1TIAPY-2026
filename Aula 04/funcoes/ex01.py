# Fibonacci: Crie uma função que recebe um número n e
# retorna o n-ésimo número da sequência de Fibonacci.

# 0 1 1 2 3 5 8 13 21 ...

def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(2, n+1):
        # soma = n1+n2
        # n1 = n2
        # n2 = soma
        n1, n2 = n2, n1 + n2
    return n2

# numero  = int(input("Digite um numero: "))

# sequencia = fibonacci(numero)
# print(f"O {numero}° numero da sequencia é: {sequencia}")

numero  = int(input("Digite um numero: "))
print(f"O {numero}° numero da sequencia é: {fibonacci(numero)}")
# Soma dos Dígitos:
# Crie uma função que recebe um
# número inteiro e retorna a soma dos seus dígitos.

def somarDigitos(n):
    resultado = 0
    for i in n:
        resultado += int(i)
    return resultado


num = input("Digite um numero inteiro: ")

print(f"A soma do numero {num} é igual a: {somarDigitos(num)}")
def gerarFatorial(num):
    if num < 1:
        print("O numero nao pode ser negativo!")
        return None

    fatorial = 1
    for i in range(2,num+1):
        fatorial *= i
    
    return fatorial

numero = int(input("Digite um numero para descobrir seu fatorial: "))
print(f"O fatorial de {numero} é {gerarFatorial(numero)}")
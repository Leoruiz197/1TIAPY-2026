soma = 0 

num = 0
while num > -1:
    soma += num
    num = int(input("Digite um numero a ser somado (-1 para encerrar): "))
    

print(f"A soma de todos os numeros digitados foi: {soma}")
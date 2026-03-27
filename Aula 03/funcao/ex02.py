def testePrimo(num):
    eh_primo = True
    for i in range(2,num):
        if num % i == 0:
            eh_primo = False
    return eh_primo

num = int(input("Digite um numero para verificar se é primo: "))

if testePrimo(num):
    print(f"O numero {num} é um numero primo!")
else:
    print(f"O numero {num} não é um numero primo!")
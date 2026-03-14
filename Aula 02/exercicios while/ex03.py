import random

num = 5
num = random.randint(1,10)

tentativas = 3

for i in range(3):
    print(f"Tentativas: {tentativas}")
    usernum = int(input("Digite um numero entre 1 e 10: "))
    while usernum > 10:
        usernum = int(input("Digite um numero entre 1 e 10: "))
    if num == usernum:
        print("Parabens voce acertou o numero!")
        break
    else:
        print("Poxa nao foi dessa vez! Tente novamente!")
    tentativas -= 1
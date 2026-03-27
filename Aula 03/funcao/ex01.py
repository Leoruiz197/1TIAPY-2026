def somar(num, num2):
    resultado = num + num2
    return resultado

def subtrair(num, num2):
    return num - num2

def multiplicar(num, num2):
    return num * num2

def dividir(num, num2):
    return num / num2

num = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

opcao = input("Digite a operação desejada ( + , - , x , /): ")

match opcao:
    case "+":
        print("Função de soma")
        soma = somar(num, num2)
        print(f"O resultado de {num} + {num2} = {soma}")
    case "-":
        print("Função de subtração")
        print(f"O resultado de {num} - {num2} = {subtrair(num,num2)}")
    case "x":
        print("Função de multiplicação")
        print(f"O resultado de {num} x {num2} = {multiplicar(num,num2)}")
    case "/":
        print("Função de divisão")
        print(f"O resultado de {num} / {num2} = {dividir(num,num2)}")
    case _ :
        print("Opção invalida, tente novamente!")
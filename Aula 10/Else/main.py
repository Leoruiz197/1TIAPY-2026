try:
    x = int(input("Digite o numerador: "))
    y = int(input("Digite o denominador: "))
    resultado = x / y
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Entrada inválida, por favor, digite números inteiros.")
else:
    print(f"Resultado: {resultado}")

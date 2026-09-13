try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

else:
    print(f"A soma de {num1} e {num2} é: {resultado}")
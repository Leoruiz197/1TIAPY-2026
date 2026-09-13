try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except ValueError:
    print("Valor inválido. Por favor, digite um número inteiro.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

else:
    print(f"O resultado da divisão é: {resultado}")
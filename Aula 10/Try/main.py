try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
finally:
    print("Bloco finally executado.")

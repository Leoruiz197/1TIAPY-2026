try:
    arquivo = input("Digite o nome do arquivo: ")

    with open(arquivo, 'r') as file:
        linhas = file.read()
        print(linhas)

except FileNotFoundError:
    print("Arquivo não encontrado.")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")

try:
    arquivo = input("Digite o nome do arquivo: ")
    with open(arquivo, 'r') as file:
        conteudo = file.readlines()

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o nome do arquivo e tente novamente.")

except Exception as e:
    print(f"Ocorreu um erro ao abrir o arquivo: {e}")

else:
    #contar linhas do arquivo lido
    num_linhas = len(conteudo)
    print(f"O arquivo '{arquivo}' contém {num_linhas} linhas.")
# Dados a serem escritos (uma lista de inteiros)
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Caminho do arquivo binário
caminho_arquivo = 'dados2.bin'

# Escrevendo no arquivo binário
with open(caminho_arquivo, 'wb') as arquivo_binario:
    for numero in numeros:
        # Convertendo cada número para binário e escrevendo no arquivo
        arquivo_binario.write(numero.to_bytes(4, byteorder='little'))

print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")

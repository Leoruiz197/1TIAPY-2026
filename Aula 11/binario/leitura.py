# Caminho do arquivo binário
caminho_arquivo = 'dados2.bin'

# Lendo o arquivo binário
with open(caminho_arquivo, 'rb') as arquivo_binario:
    numeros_lidos = []
    while True:
        # Lendo 4 bytes (tamanho de um inteiro)
        bytes_lidos = arquivo_binario.read(4)
        if not bytes_lidos:
            break
        # Convertendo de volta para um inteiro
        numero = int.from_bytes(bytes_lidos, byteorder='little')
        numeros_lidos.append(numero)

# Exibindo os números lidos
print("Números lidos do arquivo binário:", numeros_lidos)

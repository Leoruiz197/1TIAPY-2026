def xor_criptografar_dados(dados, chave):
    # Criptografa usando XOR byte a byte
    criptografado = bytearray()
    for i in range(len(dados)):
        criptografado.append(dados[i] ^ chave[i % len(chave)])  # XOR com a chave
    return criptografado

def criptografar_arquivo(arquivo_entrada, arquivo_saida, chave):
    with open(arquivo_entrada, 'rb') as f:
        conteudo = f.read()
    criptografado = xor_criptografar_dados(conteudo, chave)
    
    with open(arquivo_saida, 'wb') as f:
        f.write(criptografado)

def descriptografar_arquivo(arquivo_entrada, arquivo_saida, chave):
    criptografar_arquivo(arquivo_entrada, arquivo_saida, chave)  # XOR reversível

# Exemplo de uso
chave = b'minhachave'  # Uma chave para a criptografia
criptografar_arquivo('arquivo.txt', 'arquivo_criptografado.txt', chave)
descriptografar_arquivo('arquivo_criptografado.txt', 'arquivo_descriptografado.txt', chave)

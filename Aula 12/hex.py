def arquivo_para_hex(arquivo):
    with open(arquivo, 'rb') as f:
        conteudo = f.read()
        hex_data = conteudo.hex()
    return hex_data

# Exemplo de uso
hex_content = arquivo_para_hex('arquivo.txt')
print(f"Arquivo em hex: {hex_content}")

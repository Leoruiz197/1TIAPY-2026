def arquivo_to_hex(arquivo):
    with open(arquivo, 'rb') as f:
        conteudo = f.read()
    return " ".join(f"{byte:02x}" for byte in conteudo)

hexadecimal = arquivo_to_hex('arquivo_criptografado.txt')
print(hexadecimal)
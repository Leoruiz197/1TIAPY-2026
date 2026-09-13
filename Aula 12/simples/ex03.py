import base64

def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    base64_bytes = base64.b64encode(texto_bytes)
    return base64_bytes.decode('utf-8')

def decodificar_base64(base64_texto):
    base64_bytes = base64_texto.encode('utf-8')
    texto_bytes = base64.b64decode(base64_bytes)
    return texto_bytes.decode('utf-8')

mensagem = "Mensagem Secreta"

# Criptografar usando Base64
codificado = codificar_base64(mensagem)
print("Texto Codificado:", codificado)

# Descriptografar usando Base64
decodificado = decodificar_base64(codificado)
print("Texto Decodificado:", decodificado)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def criptografar_aes(mensagem, chave):
    iv = get_random_bytes(16)  # Gera um IV aleatório
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_preenchida = pad(mensagem.encode('utf-8'), AES.block_size)  # Padding da mensagem
    criptografado = cipher.encrypt(mensagem_preenchida)
    return iv + criptografado  # Retorna o IV concatenado com o texto criptografado

def descriptografar_aes(criptografado, chave):
    iv = criptografado[:16]  # Extrai o IV do início
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_criptografada = criptografado[16:]  # O restante é o texto criptografado
    mensagem_preenchida = cipher.decrypt(mensagem_criptografada)
    return unpad(mensagem_preenchida, AES.block_size).decode('utf-8')  # Remove o padding e retorna a mensagem original

# Exemplo de uso
mensagem = "Este é um segredo!"
chave = b"chave_secreta_16"  # Chave de 16 bytes (128 bits)

# Criptografar
criptografado = criptografar_aes(mensagem, chave)
print(f"Texto Criptografado: {criptografado.hex()}")

# Descriptografar
descriptografado = descriptografar_aes(criptografado, chave)
print(f"Texto Descriptografado: {descriptografado}")

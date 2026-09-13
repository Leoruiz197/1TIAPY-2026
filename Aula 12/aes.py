from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Função para criptografar dados usando AES
def encrypt_aes(data, key):
    # Gera um IV (Initialization Vector) aleatório de 16 bytes
    iv = get_random_bytes(16)
    
    # Inicializa o cifrador AES em modo CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Padding do dado para garantir que o tamanho seja múltiplo de 16 bytes
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    
    # Criptografa os dados
    ciphertext = cipher.encrypt(padded_data)
    
    # Retorna o IV concatenado com o texto criptografado
    return iv + ciphertext

# Função para descriptografar dados usando AES
def decrypt_aes(encrypted_data, key):
    # O IV está nos primeiros 16 bytes do dado criptografado
    iv = encrypted_data[:16]
    
    # O texto criptografado começa após o IV
    ciphertext = encrypted_data[16:]
    
    # Inicializa o decifrador AES em modo CBC com o mesmo IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Descriptografa e remove o padding
    original_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return original_data.decode('utf-8')

# Exemplo de uso
if __name__ == "__main__":
    # Chave de 16 bytes (128 bits)
    key = b'secretaechaveaes'  # precisa ter exatamente 16, 24 ou 32 bytes
    
    # Texto a ser criptografado
    texto = "Mensagem Confidencial"
    
    # Criptografa o texto
    texto_criptografado = encrypt_aes(texto, key)
    print(f"Texto criptografado (hex): {texto_criptografado.hex()}")
    
    # Descriptografa o texto
    texto_descriptografado = decrypt_aes(texto_criptografado, key)
    print(f"Texto original: {texto_descriptografado}")

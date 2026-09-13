def xor_cipher(texto, chave):
    resultado = ''.join([chr(ord(c) ^ ord(chave)) for c in texto])
    return resultado

mensagem = "Vamos guardar um segredo na aula de Python!"
chave = 'B'

# Criptografar a mensagem
criptografada = xor_cipher(mensagem, chave)
print("Texto Criptografado:", criptografada)

# Descriptografar a mensagem
original = xor_cipher(criptografada, chave)
print("Texto Original:", original)

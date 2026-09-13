def cifra_de_cesar(texto, deslocamento):
    resultado = ''
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra) + deslocamento
            if letra.islower():
                resultado += chr((codigo - 97) % 26 + 97)
            elif letra.isupper():
                resultado += chr((codigo - 65) % 26 + 65)
        else:
            resultado += letra
    return resultado

texto = "Python"
deslocamento = 3

# Criptografar o texto
criptografado = cifra_de_cesar(texto, deslocamento)
print("Texto Criptografado:", criptografado)

# Descriptografar o texto
descriptografado = cifra_de_cesar(criptografado, -deslocamento)
print("Texto Descriptografado:", descriptografado)

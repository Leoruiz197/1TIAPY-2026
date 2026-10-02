# Converter para Maiúsculas: Crie uma função que recebe
# uma string e retorna a mesma string em maiúsculas.

def converter_para_maiusculas(texto):
    textoMaiusculo = ""
    for letra in texto:
        if 'a' <= letra <= 'z':  # Verifica se a letra é minúscula
            textoMaiusculo += chr(ord(letra) - (ord('a') - ord('A')))  # Converte para maiúscula
        else:
            textoMaiusculo += letra  # Mantém caracteres que não são letras minúsculas
    return textoMaiusculo

frase = input("Digite uma frase: ")
resultado = converter_para_maiusculas(frase)
print("Frase em maiúsculas:", resultado)
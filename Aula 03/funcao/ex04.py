def contarVogais(frase):
    VOGAIS = ['a','e','i','o','u']

    contador = 0
    for letra in frase.lower():
        if letra in VOGAIS:
            contador += 1
    return contador

frase = input("Digite a frase para contarmos as vogais presentes: ")

print(f"Na frase: {frase}, existem {contarVogais(frase)} vogais!")
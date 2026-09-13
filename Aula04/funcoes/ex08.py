def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

# Exemplo de uso
texto = "Python"
num_vogais = contar_vogais(texto)
print(f"O texto '{texto}' possui {num_vogais} vogais.")

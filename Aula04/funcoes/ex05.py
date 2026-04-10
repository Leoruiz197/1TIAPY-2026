# Verificar Palíndromo: Crie uma função que recebe uma
# string e verifica se ela é um palíndromo (ou seja, se
# pode ser lida da mesma forma de trás para frente).

def verificaPalindromo(texto):
    texto = texto.replace(" ", "").lower()
    if texto[::-1] == texto:
        return True
    else:
        return False


texto = input("Digite uma frase ou palavra: ")
if verificaPalindromo(texto):
    print("A frase ou palavra usada é um palindromo")
else:
    print("A frase ou palavra usada não é um palindromo")
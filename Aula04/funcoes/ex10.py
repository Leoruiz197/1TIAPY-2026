def numeros_primos(n):
    primos = []
    # Inicialmente, assumimos que todos os números de 2 a n são primos
    eh_primo = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (eh_primo[p] == True):
            for i in range(p * p, n + 1, p):
                eh_primo[i] = False
        p += 1
    for p in range(2, n):
        if eh_primo[p]:
            primos.append(p)
    return primos

# Exemplo de uso
n = 20
lista_primos = numeros_primos(n)
print(f"Números primos até {n}: {lista_primos}")

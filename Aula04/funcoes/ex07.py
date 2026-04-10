# Calcular Média Ponderada: Crie uma função que recebe
# três notas e seus respectivos pesos, e retorna a média
# ponderada dessas notas.

def calcular_media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    total_pesos = peso1 + peso2 + peso3
    if total_pesos == 0:
        return 0  # Evita divisão por zero
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / total_pesos
    return media_ponderada

notas = []
pesos = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    peso = float(input(f"Digite o peso {i+1}: "))
    notas.append(nota)
    pesos.append(peso)

media = calcular_media_ponderada(notas[0], pesos[0], notas[1], pesos[1], notas[2], pesos[2])
print("A média ponderada é:", media)
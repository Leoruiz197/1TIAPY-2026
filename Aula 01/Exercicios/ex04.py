distancia = float(input("Digite a distancia total percorrida em Kms: ")) 
velMedia = float(input("Digite a velocidade media em Km/H: "))

tempo = distancia / velMedia
horas = int(tempo)
minutos = int((tempo - horas) * 60)

print(f"O tempo total de viagem é de: {horas}H:{minutos}m")
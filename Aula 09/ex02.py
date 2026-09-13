class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def info_basica(self):
        return f'marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    def info_basica(self):
        info = super().info_basica()
        return f'{info}, numero de portas: {self.portas}'

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def info_basica(self):
        info = super().info_basica()
        return f'{info}, cilindradas: {self.cilindradas}'
    
carro = Carro("FIAT","UNO",2000,4)
moto = Moto("HONDA","CG160",2015,160)

print(carro.info_basica())
print(moto.info_basica())
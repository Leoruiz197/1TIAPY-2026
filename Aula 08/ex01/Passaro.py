from Animal import Animal

class Passaro(Animal):
    def __init__(self, nome, especie, peso, cor):
        super().__init__(nome, especie, peso)
        self.cor = cor

    def fazerSom(self):
        return "Piu Piu"
    
    def voar(self):
        return "O pássaro está voando"
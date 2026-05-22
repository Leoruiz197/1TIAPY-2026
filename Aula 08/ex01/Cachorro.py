from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, especie, peso, raca):
        super().__init__(nome, especie, peso)
        self.raca = raca

    def fazerSom(self):
        return "Au Au"
    
    def correr(self):
        return "O cachorro está correndo"
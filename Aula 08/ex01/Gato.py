from Animal import Animal

class Gato(Animal):
    def __init__(self, nome, especie, peso, pelagem):
        super().__init__(nome, especie, peso)
        self.pelagem = pelagem

    def fazerSom(self):
        return "Miau Miau"
    
    def comer(self):
        return "O gato está comendo"
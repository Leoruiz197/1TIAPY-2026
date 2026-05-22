class Animal:
    def __init__(self, nome, especie, peso):
        self.name = nome
        self.species = especie
        self.weight = peso

    def fazerSom(self):
        return "fazer som"
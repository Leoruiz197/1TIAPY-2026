class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def infos(self):
        return f"{self.nome} - R${self.preco:.2f}"
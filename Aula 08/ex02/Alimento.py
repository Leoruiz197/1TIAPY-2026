from Produto import Produto

class Alimento(Produto):
    def __init__(self, nome, preco, validade, tipo):
        super().__init__(nome, preco)
        self.validade = validade
        self.tipo = tipo

    def infos(self):
        return f"{self.nome} - R${self.preco:.2f} - Validade: {self.validade} - Tipo: {self.tipo}"
    
    def consumir(self):
        return f"{self.nome} foi consumido."
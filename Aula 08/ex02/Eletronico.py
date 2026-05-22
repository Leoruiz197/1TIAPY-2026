from Produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, preco, marca, tensao):
        super().__init__(nome, preco)
        self.marca = marca
        self.tensao = tensao

    def infos(self):
        return f"{self.nome} - R${self.preco:.2f} - Marca: {self.marca} - Tensão: {self.tensao}"
    
    def ligar(self):
        return f"{self.nome} está ligado."
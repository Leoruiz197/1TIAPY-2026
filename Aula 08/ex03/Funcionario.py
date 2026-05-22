from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario, funcao):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
        self.funcao = funcao

    def apresentar(self):
        super().apresentar()
        print(f"Eu trabalho como {self.cargo}, recebo R${self.salario:.2f} e minha função é {self.funcao}.")
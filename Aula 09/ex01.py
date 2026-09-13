class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def info_basica(self):
        return f'Nome do funcionario: {self.nome}, salario: {self.salario} '

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome,salario)
        self.setor = setor
    def info_basica(self):
        info = super().info_basica()
        return f'{info}, Setor: {self.setor}'
    def subir_salario(self, porcentagem):
        self.salario = self.salario + ((self.salario/100) * porcentagem)
   
funcionario = Funcionario("leo",100000)
gerente = Gerente("Fabio",500000,"Controladoria")

# funcionario.info_basica()
gerente.subir_salario(10)
print(gerente.info_basica())

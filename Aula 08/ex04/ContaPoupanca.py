from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, titular, saldo, aniversario, juros):
        super().__init__(agencia, numero, titular, saldo)
        self.aniversario = aniversario
        self.juros = juros

    def mostrar_aniversario(self):
        print(f"Aniversário da conta: {self.aniversario}")

    def calcular_juros(self):
        juros_calculados = self.saldo * self.juros
        print(f"Juros calculados: {juros_calculados}")
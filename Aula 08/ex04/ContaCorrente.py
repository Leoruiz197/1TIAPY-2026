from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, titular, saldo, limite):
        super().__init__(agencia, numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
        
    def mostrar_limite(self):
        print(f"Limite disponível: {self.limite}")
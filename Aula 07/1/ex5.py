class Pessoa():
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    
    def descrever(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura} | Sexo: {self.sexo}"
    
pessoas = []

for i in range(1,6):
    pessoa = Pessoa(f"pessoa{i}",i+15,i+76,157+i,"M")
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa.descrever())

class Pessoa():
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
    
    def descrever(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura} | Sexo: {self.sexo}"
    
    def envelhecer(self):
        self.idade += 1
    
    def comparar_idade(self, pessoa):
        if self.idade > pessoa.idade:
            print(f"{self.nome} é mais velho que {pessoa.nome}")
        elif self.idade < pessoa.idade:
            print(f"{self.nome} é mais novo que {pessoa.nome}")
        else:
            print("Ambas tem a mesma idade")


pessoa = Pessoa("Leo",28, 100, 188, "M")
pessoa2 = Pessoa("Caique",20, 73, 173, "M")

pessoa.comparar_idade(pessoa2)
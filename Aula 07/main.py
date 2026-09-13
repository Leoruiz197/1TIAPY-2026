class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Peso: {self.peso} | Altura: {self.altura} | Sexo: {self.sexo}'

    def envelhecer(self):
        self.idade += 1
        print(f'{self.nome} envelheceu um ano e agora tem {self.idade} anos.')

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            return f'{self.nome} é mais velho(a) que {outra_pessoa.nome}.'
        elif self.idade < outra_pessoa.idade:
            return f'{self.nome} é mais novo(a) que {outra_pessoa.nome}.'

        return f'{self.nome} tem a mesma idade que {outra_pessoa.nome}.'


primeira_pessoa = Pessoa('João', 25, 70, 1.75, 'M')
print(primeira_pessoa.descrever())
primeira_pessoa.envelhecer()
primeira_pessoa.envelhecer()
pessoa_mais_velha = Pessoa('Maria', 30, 60, 1.65, 'F')
pessoa_mais_nova = Pessoa('Pedro', 20, 80, 1.80, 'M')
pessoa_com_a_mesma_idade = Pessoa('Ana', 27, 55, 1.60, 'F')
print(primeira_pessoa.comparar_idade(pessoa_mais_velha))
print(primeira_pessoa.comparar_idade(pessoa_mais_nova))
print(primeira_pessoa.comparar_idade(pessoa_com_a_mesma_idade))

for pessoa in [primeira_pessoa, pessoa_mais_velha, pessoa_mais_nova, pessoa_com_a_mesma_idade]:
    print(pessoa.descrever())
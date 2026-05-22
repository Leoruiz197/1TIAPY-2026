from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, curso, matricula, media):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
        self.media = media

    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um aluno do curso de {self.curso} e minha matrícula é {self.matricula}.  Minha média é {self.media:.2f}.")
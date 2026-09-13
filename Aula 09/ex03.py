class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    def alterar_nota(self, Aluno, nota):
        Aluno.nota = nota
    
aluno = Aluno("Renato", 54, 9.5)
professor = Professor("Leo", 76, "Cyber")

professor.alterar_nota(aluno,10)

print(aluno.nota)

class Cliente:
    def __init__(self, nome, email, telefone, endereco, _id=None):
        self._id = _id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco
        }
import mongomock
import pytest

from services.clientes import Clientes


class ConexaoTeste:
    def __init__(self):
        self.cliente = mongomock.MongoClient()
        self.db = self.cliente["teste_clientes"]

    def get_collection(self, nome):
        return self.db[nome]

    def fechar_conexao(self):
        self.cliente.close()


@pytest.fixture
def sistema():
    sistema = Clientes(conexao=ConexaoTeste())
    yield sistema
    sistema.fechar_conexao()

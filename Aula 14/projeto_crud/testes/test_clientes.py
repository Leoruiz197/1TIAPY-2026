import pytest
from src.sistema_clientes import SistemaClientes

@pytest.fixture
def sistema():
    return SistemaClientes()

def test_inserir_cliente(sistema):
    cliente = {"nome":"Leo","email":"leoteste@teste.com","telefone":"1199999-9999","endereco":"rua teste, 1000"}
    sistema.inserir_cliente(cliente)
    assert sistema.consultar_cliente(cliente['_id']) == cliente
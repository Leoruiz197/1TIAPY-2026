from models.cliente import Cliente


def test_inserir_cliente(sistema):
    cliente = Cliente(
        nome="Leonardo",
        email="leo@teste.com",
        telefone="11999999999",
        endereco="Rua Teste, 100"
    )

    cliente_id = sistema.inserir_cliente(cliente)

    assert cliente_id is not None


def test_consultar_cliente(sistema):
    cliente = Cliente(
        nome="Maria",
        email="maria@teste.com",
        telefone="11888888888",
        endereco="Rua A, 200"
    )

    cliente_id = sistema.inserir_cliente(cliente)

    cliente_encontrado = sistema.consultar_cliente(cliente_id)

    assert cliente_encontrado is not None
    assert cliente_encontrado["nome"] == "Maria"
    assert cliente_encontrado["email"] == "maria@teste.com"


def test_atualizar_cliente(sistema):
    cliente = Cliente(
        nome="Carlos",
        email="carlos@teste.com",
        telefone="11777777777",
        endereco="Rua B, 300"
    )

    cliente_id = sistema.inserir_cliente(cliente)

    novos_dados = {
        "telefone": "11666666666"
    }

    sistema.atualizar_cliente(cliente_id, novos_dados)

    cliente_atualizado = sistema.consultar_cliente(cliente_id)

    assert cliente_atualizado["telefone"] == "11666666666"


def test_deletar_cliente(sistema):
    cliente = Cliente(
        nome="Ana",
        email="ana@teste.com",
        telefone="11555555555",
        endereco="Rua C, 400"
    )

    cliente_id = sistema.inserir_cliente(cliente)

    sistema.deletar_cliente(cliente_id)

    cliente_encontrado = sistema.consultar_cliente(cliente_id)

    assert cliente_encontrado is None


def test_consultar_todos(sistema):
    cliente1 = Cliente(
        nome="Joao",
        email="joao@teste.com",
        telefone="11444444444",
        endereco="Rua D, 500"
    )

    cliente2 = Cliente(
        nome="Pedro",
        email="pedro@teste.com",
        telefone="11333333333",
        endereco="Rua E, 600"
    )

    sistema.inserir_cliente(cliente1)
    sistema.inserir_cliente(cliente2)

    clientes = sistema.consultar_todos()

    assert len(clientes) == 2

from unittest.mock import patch

import pytest
from pymongo.errors import ServerSelectionTimeoutError

from main import create_app


@pytest.fixture
def api(sistema):
    app = create_app({"TESTING": True, "CLIENTES_FACTORY": lambda: sistema})
    return app.test_client()


@pytest.fixture
def dados():
    return {
        "nome": "Maria",
        "email": "maria@teste.com",
        "telefone": "11999999999",
        "endereco": "Rua A, 100"
    }


def test_crud_completo(api, dados):
    assert api.get("/clientes").get_json() == []
    resposta = api.post("/clientes", json=dados)
    assert resposta.status_code == 201
    cliente = resposta.get_json()
    assert len(cliente["_id"]) == 24
    rota = resposta.headers["Location"]
    assert api.get(rota).get_json() == {"_id": cliente["_id"], **dados}
    assert api.get("/clientes").get_json() == [cliente]

    resposta = api.patch(rota, json={"telefone": "11888888888"})
    assert resposta.status_code == 200
    assert resposta.get_json()["telefone"] == "11888888888"
    assert resposta.get_json()["nome"] == dados["nome"]

    novos_dados = {**dados, "nome": "Ana"}
    resposta = api.put(rota, json=novos_dados)
    assert resposta.status_code == 200
    assert resposta.get_json() == {"_id": cliente["_id"], **novos_dados}
    assert api.put(rota, json=novos_dados).status_code == 200
    resposta = api.delete(rota)
    assert resposta.status_code == 204
    assert resposta.data == b""
    assert api.get(rota).status_code == 404
    assert api.get("/clientes").get_json() == []


@pytest.mark.parametrize("corpo", [None, [], {}, {"nome": "Ana"},
    {"nome": "", "email": "a@b.com", "telefone": "1", "endereco": "Rua A"},
    {"nome": "Ana", "email": "a@b.com", "telefone": 123, "endereco": "Rua A"},
    {"nome": "Ana", "email": "a@b.com", "telefone": "1", "endereco": "Rua A", "_id": "x"}
])
def test_rejeitar_corpo_invalido(api, corpo):
    resposta = api.post("/clientes", json=corpo, content_type="application/json")
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()
    assert api.get("/clientes").get_json() == []


def test_formato_json(api):
    assert api.post("/clientes", data="texto").status_code == 415
    resposta = api.post("/clientes", data="{", content_type="application/json")
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()


@pytest.mark.parametrize("metodo", ["GET", "PUT", "PATCH", "DELETE"])
def test_ids_invalidos_e_inexistentes(api, dados, metodo):
    resposta = api.open("/clientes/invalido", method=metodo, json=dados)
    assert resposta.status_code == 400
    resposta = api.open("/clientes/000000000000000000000000", method=metodo, json=dados)
    assert resposta.status_code == 404
    assert "erro" in resposta.get_json()


def test_atualizacao_invalida_nao_altera_cliente(api, dados):
    rota = api.post("/clientes", json=dados).headers["Location"]
    assert api.put(rota, json={"nome": "Ana"}).status_code == 400
    assert api.patch(rota, json={}).status_code == 400
    assert api.patch(rota, json={"$set": {"nome": "Ana"}}).status_code == 400
    assert api.get(rota).get_json()["nome"] == "Maria"


def test_erros_de_rotas_em_json(api):
    assert api.get("/").status_code == 200
    resposta = api.get("/inexistente")
    assert resposta.status_code == 404
    assert "erro" in resposta.get_json()
    resposta = api.delete("/clientes")
    assert resposta.status_code == 405
    assert "erro" in resposta.get_json()
    assert "GET" in resposta.headers["Allow"]


def test_banco_indisponivel(api, sistema):
    with patch.object(sistema, "consultar_todos", side_effect=ServerSelectionTimeoutError("teste")):
        resposta = api.get("/clientes")
    assert resposta.status_code == 503
    assert "erro" in resposta.get_json()

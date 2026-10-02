from bson.objectid import ObjectId
from flask import Blueprint, abort, current_app, g, jsonify, request, url_for

from models.cliente import Cliente
from services.clientes import Clientes


clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")
CAMPOS = {"nome", "email", "telefone", "endereco"}


def get_sistema():
    if "sistema" not in g:
        fabrica = current_app.config.get("CLIENTES_FACTORY", Clientes)
        g.sistema = fabrica()
    return g.sistema


def fechar_sistema(erro=None):
    sistema = g.pop("sistema", None)
    if sistema is not None:
        sistema.fechar_conexao()


def serializar(cliente):
    return {**cliente, "_id": str(cliente["_id"])}


def validar_id(cliente_id):
    if not ObjectId.is_valid(cliente_id):
        abort(400, description="ID de cliente inválido: use 24 caracteres hexadecimais.")


def ler_dados(parcial=False):
    if not request.is_json:
        abort(415, description="Envie o corpo com Content-Type: application/json.")
    dados = request.get_json()
    if not isinstance(dados, dict) or not dados:
        abort(400, description="Envie um objeto JSON não vazio.")
    desconhecidos = dados.keys() - CAMPOS
    if desconhecidos:
        abort(400, description="Campos desconhecidos: " + ", ".join(sorted(desconhecidos)))
    faltantes = CAMPOS - dados.keys()
    if not parcial and faltantes:
        abort(400, description="Campos obrigatórios: " + ", ".join(sorted(faltantes)))
    for campo, valor in dados.items():
        if not isinstance(valor, str) or not valor.strip():
            abort(400, description=f"O campo {campo} deve ser um texto não vazio.")
    return {campo: valor.strip() for campo, valor in dados.items()}


@clientes_bp.get("")
def listar_clientes():
    return jsonify([serializar(cliente) for cliente in get_sistema().consultar_todos()])


@clientes_bp.post("")
def criar_cliente():
    dados = ler_dados()
    cliente_id = get_sistema().inserir_cliente(Cliente(**dados))
    resposta = jsonify({"_id": str(cliente_id), **dados})
    resposta.status_code = 201
    resposta.headers["Location"] = url_for("clientes.buscar_cliente", cliente_id=str(cliente_id))
    return resposta


@clientes_bp.get("/<cliente_id>")
def buscar_cliente(cliente_id):
    validar_id(cliente_id)
    cliente = get_sistema().consultar_cliente(cliente_id)
    if cliente is None:
        abort(404, description="Cliente não encontrado.")
    return jsonify(serializar(cliente))


@clientes_bp.route("/<cliente_id>", methods=["PUT", "PATCH"])
def atualizar_cliente(cliente_id):
    validar_id(cliente_id)
    dados = ler_dados(parcial=request.method == "PATCH")
    resultado = get_sistema().atualizar_cliente(cliente_id, dados)
    if resultado.matched_count == 0:
        abort(404, description="Cliente não encontrado.")
    return buscar_cliente(cliente_id)


@clientes_bp.delete("/<cliente_id>")
def deletar_cliente(cliente_id):
    validar_id(cliente_id)
    resultado = get_sistema().deletar_cliente(cliente_id)
    if resultado.deleted_count == 0:
        abort(404, description="Cliente não encontrado.")
    return "", 204

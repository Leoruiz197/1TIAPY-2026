import json
import subprocess
import sys
from pathlib import Path

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo.errors import PyMongoError

from models.cliente import Cliente
from services.clientes import Clientes


CAMPOS = ("nome", "email", "telefone", "endereco")


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("O valor não pode ficar vazio.")


def ler_id():
    cliente_id = input("ID do cliente: ").strip()
    if not ObjectId.is_valid(cliente_id):
        print("ID inválido. Informe os 24 caracteres hexadecimais do cliente.")
        return None
    return cliente_id


def exibir_cliente(cliente):
    if cliente is None:
        print("Cliente não encontrado.")
        return
    dados = {**cliente, "_id": str(cliente["_id"])}
    print(json.dumps(dados, ensure_ascii=False, indent=2))


def cadastrar_cliente(sistema):
    dados = {campo: ler_texto(f"{campo.capitalize()}: ") for campo in CAMPOS}
    cliente_id = sistema.inserir_cliente(Cliente(**dados))
    print(f"Cliente cadastrado com o ID {cliente_id}.")


def listar_clientes(sistema):
    clientes = sistema.consultar_todos()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print(f"\n{len(clientes)} cliente(s) encontrado(s):")
    for cliente in clientes:
        exibir_cliente(cliente)


def consultar_cliente(sistema):
    cliente_id = ler_id()
    if cliente_id:
        exibir_cliente(sistema.consultar_cliente(cliente_id))


def atualizar_cliente(sistema):
    cliente_id = ler_id()
    if not cliente_id:
        return
    cliente = sistema.consultar_cliente(cliente_id)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    print("Digite os novos valores ou pressione Enter para manter o valor atual.")
    atualizacoes = {}
    for campo in CAMPOS:
        valor = input(f"{campo.capitalize()} [{cliente[campo]}]: ").strip()
        if valor:
            atualizacoes[campo] = valor
    if not atualizacoes:
        print("Nenhuma alteração informada.")
        return

    sistema.atualizar_cliente(cliente_id, atualizacoes)
    print("Cliente atualizado:")
    exibir_cliente(sistema.consultar_cliente(cliente_id))


def deletar_cliente(sistema):
    cliente_id = ler_id()
    if not cliente_id:
        return
    cliente = sistema.consultar_cliente(cliente_id)
    if cliente is None:
        print("Cliente não encontrado.")
        return
    confirmacao = input(f"Excluir {cliente['nome']}? [s/N]: ").strip().lower()
    if confirmacao != "s":
        print("Exclusão cancelada.")
        return
    sistema.deletar_cliente(cliente_id)
    print("Cliente excluído.")


def executar_testes():
    print("\nExecutando os testes automatizados...\n", flush=True)
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "testes", "-v"],
        cwd=Path(__file__).resolve().parent,
        check=False
    )
    if resultado.returncode == 0:
        print("\nTodos os testes passaram.")
    else:
        print(f"\nOs testes terminaram com o código {resultado.returncode}.")


def exibir_menu():
    print("""
=== SISTEMA DE CLIENTES ===
1 - Cadastrar cliente
2 - Listar clientes
3 - Consultar cliente por ID
4 - Atualizar cliente
5 - Excluir cliente
6 - Executar testes automatizados
0 - Sair
""")


def executar_menu():
    load_dotenv()
    sistema = Clientes()
    try:
        while True:
            exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            try:
                match opcao:
                    case "1":
                        cadastrar_cliente(sistema)
                    case "2":
                        listar_clientes(sistema)
                    case "3":
                        consultar_cliente(sistema)
                    case "4":
                        atualizar_cliente(sistema)
                    case "5":
                        deletar_cliente(sistema)
                    case "6":
                        executar_testes()
                    case "0":
                        print("Sistema encerrado.")
                        break
                    case _:
                        print("Opção inválida. Escolha um número do menu.")
            except PyMongoError as erro:
                print(f"Não foi possível acessar o MongoDB: {erro}")
    except (EOFError, KeyboardInterrupt):
        print("\nSistema encerrado.")
    finally:
        sistema.fechar_conexao()


if __name__ == "__main__":
    executar_menu()

from bson.objectid import ObjectId

from database.conexao import ConexaoMongo
from models.cliente import Cliente


class Clientes:
    def __init__(self):
        self.conexao = ConexaoMongo()
        self.colecao = self.conexao.get_collection("clientes")

    def inserir_cliente(self, cliente: Cliente):
        resultado = self.colecao.insert_one(cliente.to_dict())
        return resultado.inserted_id

    def atualizar_cliente(self, cliente_id, dados_atualizados):
        return self.colecao.update_one(
            {"_id": ObjectId(cliente_id)},
            {"$set": dados_atualizados}
        )

    def deletar_cliente(self, cliente_id):
        return self.colecao.delete_one(
            {"_id": ObjectId(cliente_id)}
        )

    def consultar_cliente(self, cliente_id):
        return self.colecao.find_one(
            {"_id": ObjectId(cliente_id)}
        )

    def consultar_todos(self):
        return list(self.colecao.find())

    def fechar_conexao(self):
        self.conexao.fechar_conexao()
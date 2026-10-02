from pymongo import MongoClient
from bson.objectid import ObjectId

class SistemaClientes:
    def __init__(self, db_name='sistema_clientes', collection_name="clientes"):
        self.cliente = MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente[db_name]
        self.colecao = self.db[collection_name]

    def inserir_cliente(self, client):
        self.colecao.insert_one(client)

    def atualizar_cliente(self, cliente_id, dados_atualizados):
        self.colecao.update_one({'_id': ObjectId(cliente_id)}, {'$set': dados_atualizados})

    def deletar_cliente(self, cliente_id):
        self.colecao.delete_one({'_id': ObjectId(cliente_id)})

    def consultar_cliente(self, cliente_id):
        return self.colecao.find_one({'_id': ObjectId(cliente_id)})

    def consultar_todos(self):
        return list(self.colecao.find())
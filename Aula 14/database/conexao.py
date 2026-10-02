from pymongo import MongoClient

class ConexaoMongo:
    def __init__(self, db_name="sistema_clientes"):
        self.cliente = MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def fechar_conexao(self):
        self.cliente.close()
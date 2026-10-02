import os

from pymongo import MongoClient

class ConexaoMongo:
    def __init__(self, db_name=None, uri=None):
        self.cliente = MongoClient(
            uri or os.getenv("MONGO_URI", "mongodb://localhost:27017/"),
            serverSelectionTimeoutMS=5000
        )
        self.db = self.cliente[db_name or os.getenv("MONGO_DB", "sistema_clientes")]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def fechar_conexao(self):
        self.cliente.close()

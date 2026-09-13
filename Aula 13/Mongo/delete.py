from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente['FIAP']

colecao = db['alunos']

# Deletar um documento
colecao.delete_one({"nome": {"$regex": "Maria.*"}})
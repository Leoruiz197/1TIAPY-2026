from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente['FIAP']

colecao = db['alunos']

# Atualizar o primeiro documento que encontrar com o nome "João"
colecao.update_one({"idade": 35}, {"$set": {"idade": 25}})

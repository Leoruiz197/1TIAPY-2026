from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente['FIAP']

colecao = db['alunos']

# Buscar todos os documentos
for doc in colecao.find():
    print(doc)

# Buscar documentos com critério
resultado = colecao.find({"nome": {"$regex": "Maria.*"}})
for doc in resultado:
    print(doc)

from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente['FIAP']

colecao = db['alunos']

# Inserir um documento
documento = {"nome": "João", "idade": 30}
colecao.insert_one(documento)

# Inserir vários documentos
documentos = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Pedro", "idade": 35}
]
colecao.insert_many(documentos)

from pymongo import MongoClient

# Conectar ao MongoDB local (localhost na porta 27017)
cliente = MongoClient("mongodb://localhost:27017/")

# Alternativa para MongoDB Atlas (na nuvem)
# Substitua '<USERNAME>', '<PASSWORD>' e '<CLUSTER>' pelos seus dados de conexão do Atlas
# cliente = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Escolher ou criar o banco de dados
db = cliente['FIAP']

# Escolher ou criar a coleção (similar a tabelas no SQL)
colecao = db['alunos']

# Exemplo de inserção de um documento na coleção
documento = {
    "nome": "Maria Clara",
    "idade": 16,
    "cidade": "Rio de Janeiro"
}

# Inserir o documento na coleção
resultado = colecao.insert_one(documento)
print(f"Documento inserido com ID: {resultado.inserted_id}")

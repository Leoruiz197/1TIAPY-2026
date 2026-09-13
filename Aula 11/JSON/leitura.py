import json

# Caminho do arquivo JSON
caminho_arquivo = 'dados.json'

# Lendo o arquivo JSON
with open(caminho_arquivo, 'r') as arquivo_json:
    dados = json.load(arquivo_json)

# Iterando sobre os dados lidos
for pessoa in dados['pessoas']:
    nome = pessoa['nome']
    idade = pessoa['idade']
    profissao = pessoa['profissao']
    cidade = pessoa['cidade']
    pais = pessoa['pais']
    
    print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Cidade: {cidade}, País: {pais}")

import json

# Dicionário Python
dados = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "Sao Paulo"
}

# Convertendo para JSON
json_dados = json.dumps(dados)
print(json_dados)

# Convertendo de JSON para Python
dados_python = json.loads(json_dados)
print(dados_python)

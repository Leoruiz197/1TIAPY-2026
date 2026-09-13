import json

# Dados para serem escritos no arquivo JSON
dados = {
    "pessoas": [
        {
            "nome": "João",
            "idade": 30,
            "profissao": "Engenheiro",
            "cidade": "São Paulo",
            "pais": "Brasil"
        },
        {
            "nome": "Maria",
            "idade": 25,
            "profissao": "Médica",
            "cidade": "Lisboa",
            "pais": "Portugal"
        },
        {
            "nome": "Carlos",
            "idade": 40,
            "profissao": "Professor",
            "cidade": "Madrid",
            "pais": "Espanha"
        },
        {
            "nome": "Ana",
            "idade": 35,
            "profissao": "Arquiteta",
            "cidade": "Paris",
            "pais": "França"
        }
    ]
}

# Caminho do arquivo JSON
caminho_arquivo = 'novos_dados.json'

# Escrevendo no arquivo JSON
with open(caminho_arquivo, 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=2)

print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")

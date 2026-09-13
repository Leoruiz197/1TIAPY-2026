import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('FIAP.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar tabela no banco de dados
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')

# Confirmar a criação da tabela
conn.commit()

# Fechar a conexão
conn.close()

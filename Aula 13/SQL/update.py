import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('FIAP.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Atualizar o nome de um aluno
cursor.execute('''
UPDATE alunos 
SET idade = 16 
WHERE id = 3
''')

conn.commit()

# Fechar a conexão
conn.close()

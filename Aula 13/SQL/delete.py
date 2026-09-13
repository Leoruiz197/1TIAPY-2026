import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('FIAP.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Deletar um aluno
cursor.execute('''
DELETE FROM alunos 
WHERE id = 1
''')

conn.commit()

# Fechar a conexão
conn.close()

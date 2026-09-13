import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('FIAP.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Inserir um novo registro
cursor.execute('''
INSERT INTO alunos (nome, idade) 
VALUES ('Augusto', 74)
''')

# Confirmar a inserção
conn.commit()

# Fechar a conexão
conn.close()

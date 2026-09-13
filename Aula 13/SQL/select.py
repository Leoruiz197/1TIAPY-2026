import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('FIAP.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Selecionar todos os registros da tabela
cursor.execute('SELECT * FROM alunos')

# Recuperar todos os resultados
alunos = cursor.fetchall()

# Exibir resultados
for aluno in alunos:
    print(aluno)

# Fechar a conexão
conn.close()

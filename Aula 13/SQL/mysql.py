import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="sua_senha",
        database="nome_do_banco"
    )
    
    if conexao.is_connected():
        print("Conectado ao banco de dados com sucesso!")

except Exception as erro:
    print(f"Erro ao conectar: {erro}")

finally:
    # Fecha a conexão ao terminar
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão fechada.")
from models.cliente import Cliente
from services.clientes import Clientes


sistema = Clientes()

cliente = Cliente(
    nome="Leonardo",
    email="leo@teste.com",
    telefone="11999999999",
    endereco="Rua Teste, 100"
)

cliente_id = sistema.inserir_cliente(cliente)

print("Cliente cadastrado:", cliente_id)

cliente_encontrado = sistema.consultar_cliente(cliente_id)

print(cliente_encontrado)

sistema.fechar_conexao()
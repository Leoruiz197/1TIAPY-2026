# API REST de clientes

API Flask com persistência em MongoDB. O `main.py` cria a aplicação e registra
as rotas de `routes/clientes.py`; `services/clientes.py` executa o CRUD e
`database/conexao.py` configura a conexão. Importar a aplicação não cadastra clientes.

## Executar

Na pasta `Aula 14`, instale as dependências e inicie a aplicação:

```powershell
python -m pip install -r requirements.txt
python main.py
```

A API estará em `http://127.0.0.1:5000`. É necessário ter o MongoDB em execução.
Por padrão, usa `mongodb://localhost:27017/`, banco `sistema_clientes` e coleção
`clientes`. As configurações ficam no arquivo `.env`, carregado automaticamente:

```dotenv
MONGO_URI=mongodb://localhost:27017/
MONGO_DB=sistema_clientes
```

O `.env` está ignorado pelo Git para não publicar credenciais. O arquivo
`.env.example` contém o modelo que pode ser versionado e compartilhado. Em outro
ambiente, crie o `.env` a partir dele e ajuste principalmente `MONGO_URI`.

Para desenvolvimento com recarga automática:

```powershell
python -m flask --app main run --debug
```

## Menu no terminal

O `main2.py` oferece acesso ao mesmo CRUD por um menu feito com `match/case`:

```powershell
python main2.py
```

O menu permite cadastrar, listar, consultar, atualizar e excluir clientes. Para
consultas, alterações e exclusões, informe o `_id` exibido no cadastro ou na
listagem. Na atualização, pressione Enter para manter o valor atual. A exclusão
exige confirmação.

A opção `6 - Executar testes automatizados` chama `python -m pytest testes -v`
com o mesmo interpretador usado pelo menu e informa se a suíte passou. O CRUD do
terminal usa as configurações MongoDB do `.env`; os testes permanecem isolados
em memória.

## Rotas

| Método | Rota | Operação | Sucesso |
| --- | --- | --- | --- |
| GET | `/` | Apresenta as rotas | 200 |
| GET | `/clientes` | Lista clientes (array JSON) | 200 |
| POST | `/clientes` | Cria um cliente | 201 |
| GET | `/clientes/<cliente_id>` | Consulta um cliente | 200 |
| PUT | `/clientes/<cliente_id>` | Atualiza os quatro campos | 200 |
| PATCH | `/clientes/<cliente_id>` | Atualiza apenas os campos enviados | 200 |
| DELETE | `/clientes/<cliente_id>` | Exclui um cliente | 204, sem corpo |

Use `Content-Type: application/json` para POST, PUT e PATCH. POST e PUT exigem
`nome`, `email`, `telefone` e `endereco`. Todos devem ser textos não vazios;
telefone deve ser enviado entre aspas. PATCH exige pelo menos um desses campos.
Campos desconhecidos são rejeitados. Espaços nas extremidades são removidos.

Exemplo de corpo para POST ou PUT:

```json
{
  "nome": "Maria",
  "email": "maria@teste.com",
  "telefone": "11999999999",
  "endereco": "Rua A, 100"
}
```

A resposta de criação contém esses campos e `_id` como string. O cabeçalho
`Location` aponta para a consulta do novo cliente. Use esse `_id` nas demais rotas.

### Exemplo no PowerShell

```powershell
$corpo = @{
    nome = "Maria"
    email = "maria@teste.com"
    telefone = "11999999999"
    endereco = "Rua A, 100"
} | ConvertTo-Json

$cliente = Invoke-RestMethod -Uri "http://127.0.0.1:5000/clientes" -Method Post -ContentType "application/json" -Body $corpo
Invoke-RestMethod -Uri "http://127.0.0.1:5000/clientes"
Invoke-RestMethod -Uri "http://127.0.0.1:5000/clientes/$($cliente._id)"
Invoke-RestMethod -Uri "http://127.0.0.1:5000/clientes/$($cliente._id)" -Method Patch -ContentType "application/json" -Body '{"telefone":"11888888888"}'
Invoke-RestMethod -Uri "http://127.0.0.1:5000/clientes/$($cliente._id)" -Method Delete
```

### Erros

As respostas de erro seguem o formato `{"erro": "Descrição do problema"}`:

- **400**: JSON, campos ou ID inválidos (o ID deve ter 24 caracteres hexadecimais).
- **404**: cliente ou rota não encontrado.
- **405**: método não permitido para a rota.
- **415**: corpo enviado sem o tipo `application/json`.
- **503**: falha de acesso ao MongoDB.
- **500**: erro interno inesperado.

## Testes

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest testes -v
```

Os testes de serviço e dos endpoints usam MongoDB simulado em memória
(`mongomock`), com uma instância isolada por teste. Não exigem um servidor MongoDB
nem acessam os dados da aplicação. A conexão com MongoDB real deve ser verificada
no ambiente em que a API será executada.

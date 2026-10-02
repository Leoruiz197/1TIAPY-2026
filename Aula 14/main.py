from flask import Flask, jsonify
from dotenv import load_dotenv
from pymongo.errors import PyMongoError
from werkzeug.exceptions import HTTPException

from routes.clientes import clientes_bp, fechar_sistema


load_dotenv()


def create_app(config=None):
    app = Flask(__name__)
    app.json.ensure_ascii = False
    if config:
        app.config.update(config)

    app.register_blueprint(clientes_bp)
    app.teardown_appcontext(fechar_sistema)

    @app.get("/")
    def inicio():
        return jsonify({
            "mensagem": "API de clientes",
            "rotas": {
                "/clientes": ["GET", "POST"],
                "/clientes/<cliente_id>": ["GET", "PUT", "PATCH", "DELETE"]
            }
        })

    @app.errorhandler(HTTPException)
    def erro_http(erro):
        resposta = erro.get_response()
        resposta.data = app.json.dumps({"erro": erro.description})
        resposta.content_type = "application/json"
        return resposta

    @app.errorhandler(PyMongoError)
    def erro_banco(erro):
        app.logger.exception("Erro ao acessar o MongoDB")
        return jsonify({"erro": "Não foi possível acessar o banco de dados."}), 503

    @app.errorhandler(500)
    def erro_interno(erro):
        return jsonify({"erro": "Erro interno do servidor."}), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

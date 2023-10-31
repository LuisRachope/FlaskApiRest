from flask import Flask

from src.repository.database_respository import DatabaseRepository
from src.routes.user_routes import user as user_routes

dba = DatabaseRepository()


def init_app():
    """Inicialização do core da Aplicação"""
    app = Flask(__name__, instance_relative_config=False)

    if dba.connect_db() == None:
        dba.create_table("user")
        dba.insert_table("user")
        dba.select_table("user")

    with app.app_context():
        app.register_blueprint(user_routes)

        return app


app = init_app()

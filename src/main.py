from flask import Flask
from src.routes.user_routes import user as user_routes
from src.data.create_db import Database

dba = Database()

def init_app():
    """Inicialização do core da Aplicação"""
    app = Flask(__name__, instance_relative_config=False)

    if dba.connect_db() == None:
        dba.create_table('user')
        dba.insert_table('user')
        dba.select_table('user')

    with app.app_context():
        app.register_blueprint(user_routes)

        return app
    
app = init_app()
#ctx = app.app_context()



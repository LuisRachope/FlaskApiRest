from flask import Flask
from src.routes.user_routes import user as user_routes

def init_app():
    """Inicialização do core da Aplicação"""
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        app.register_blueprint(user_routes)

        return app
    
app = init_app()
#ctx = app.app_context()
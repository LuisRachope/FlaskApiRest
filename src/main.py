from flask import Flask, Blueprint
from routes.user_routes import user as user_routes

# Globally accessible libraries

def init_app():
    """Inicialização do core da Aplicação"""
    app = Flask(__name__, instance_relative_config=False)
    #app.config.from_object('config.Config')

    # Initialize Plugins
    #user.init_app(app)
    #data.init_app(app) 

    with app.app_context():
        # Include our Routes
        #from . import routes

        # Register Blueprints
        app.register_blueprint(user_routes)

        return app
        
if __name__ == '__main__':
	init_app().run(debug=True)
    
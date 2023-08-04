from flask import Blueprint

index = Blueprint('routes', __name__)

@index.route('/')
def index_page():
    return "<h2>Bem-Vindo à API Flask WSGI<h2>", 200
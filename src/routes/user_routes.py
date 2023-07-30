from flask import jsonify, Blueprint
from src.repository.user_repository import UserRepository

user = Blueprint('server', __name__, url_prefix='/user')
user_repository = UserRepository()

@user.route('/get_all')
def get_all():
    data = user_repository.read_all()
    return jsonify(data)

@user.route('/<int:id>')
def get_by_id(id):
    data = user_repository.read_by_id(id)
    return jsonify(data)
from flask import jsonify, Blueprint, request
from src.controller.user_controller import UserController

user = Blueprint('server', __name__, url_prefix='/user')
user_controller = UserController()

@user.route('/get_all', methods=['GET'])
def user_get_all():
    data = user_controller.get_users_all()
    return jsonify(data), 200

@user.route('/<int:id>', methods=['GET'])
def user_by_id(id):
    data = user_controller.get_user_by_id(id)
    return jsonify(data), 200

@user.route('/create', methods=['POST'])
def create_new_user():
    body = request.json
    response = user_controller.create_user(body)
    return jsonify(response), 200
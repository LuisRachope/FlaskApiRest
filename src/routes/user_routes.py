from flask import Blueprint, jsonify, request, send_file

from src.controller.user_controller import UserController
from src.core.utils.buffer_file import create_buffer_stream

user = Blueprint("server", __name__, url_prefix="/user")
user_controller = UserController()


@user.route("/get_all", methods=["GET"])
def user_get_all():
    data = user_controller.get_users_all()
    return jsonify(data), 200


@user.route("/<int:id>", methods=["GET"])
def user_by_id(id):
    data = user_controller.get_user_by_id(id)
    return jsonify(data), 200


@user.route("/create", methods=["POST"])
def create_new_user():
    body = request.json
    response = user_controller.create_user(body)
    return jsonify(response), 200


@user.route("/file", methods=["GET"])
def create_file_user():
    data = {"id": 1001, "name": "Teste de Buffer para o GET", "age": 27, "email": "teste@email.com"}

    buffer = create_buffer_stream(file_data=data)

    # Utiliza a função send_file do Flask para enviar o arquivo na response para download
    return send_file(buffer, as_attachment=True, download_name="arquivo.json", mimetype="application/json"), 200

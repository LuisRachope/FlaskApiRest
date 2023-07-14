from flask import jsonify, request
from service.Database import Database

class UserController:
    def __init__(self) -> None:
        self.db = Database()

    def GetById(self, id):
        data = self.db.ReadByName(id)
        return jsonify(data)
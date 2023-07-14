from flask import jsonify, request
from service.Database import Database

class DataController:
    def __init__(self) -> None:
        self.db = Database()

    def GetAll(self):
        data = self.db.ReadAll()
        return jsonify(data)
from flask import Flask, jsonify, request
from controller.users import UserController
from controller.data import DataController

app = Flask(__name__)
users = UserController()
allInfo = DataController()

@app.route('/get_all', methods=['GET'])
def GetAll():
	if(request.method == 'GET'):
		return allInfo.GetAll()
	
@app.route('/get_user/<int:id>', methods=['GET'])
def GetById(id):
	if(request.method == 'GET'):
		return users.GetById(id)

if __name__ == '__main__':
	app.run(debug=True)
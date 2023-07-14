from flask import Flask, jsonify, request
from service.Database import Database

app = Flask(__name__)

@app.route('/get_all', methods=['GET'])
def GetAll():
	db = Database()
	if(request.method == 'GET'):
		data = db.ReadAll()
		return jsonify(data)
	
@app.route('/get_users/<int:id>', methods=['GET'])
def GetUsers(id):
	db = Database()
	if(request.method == 'GET'):
		data = db.ReadByName(id)
		return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)
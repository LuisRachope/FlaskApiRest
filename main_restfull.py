from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
	def get(self):
		data={"data":"Hello World"}
		return data

api.add_resource(HelloWorld,'/get_response')

if __name__=='__main__':
	app.run(debug=True)
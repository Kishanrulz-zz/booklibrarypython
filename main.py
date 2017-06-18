from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'library'
app.config['MONGO_URI'] = 'mongodb://localhost'


mongo = PyMongo(app)

@app.route('/user', methods = ['POST'])
def create_user():
	users = mongo.db.users
	name = request.json['name']
	gender = request.json['gender']
	age = request.json['age']
	status = True
	print(name)
	user_id = users.insert({'name' : name, 'gender' : gender, 'age' : age, 'status' : status})
	return jsonify({'user_id' : 'user created successfully'})


if __name__ == '__main__':
    app.run(debug=True)

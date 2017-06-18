from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId # For ObjectId to work


app = Flask(__name__)

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.library    #Select the database
users = db.users #Select the collection
books = db.books



@app.route('/user', methods = ['POST'])
def create_user():
	name = request.json['name']
	gender = request.json['gender']
	age = request.json['age']
	status = True
	print(name)
	user = users.insert({'name' : name, 'gender' : gender, 'age' : age, 'status' : status})
	return jsonify({'result' : 'user created successfully'})


@app.route('/user/<user_id>', methods = ['GET'])
def find_user(user_id):
	print(user_id)
	if ObjectId.is_valid(user_id) == False:
		output = {'message' : 'Sorry, invalid userID'}
		return jsonify({'result' : output})

	id = ObjectId(user_id)
	user = users.find_one({'_id' : id})
	print(user['name'])
	if user:
		print("Exists")
		output = {'name' : user['name'], 'gender' : user['gender'], 'age' : user['age'], 'status' : user['status'], 'id' : str(user['_id'])}
	else:
		output = {'message' : 'Sorry, user does not exists'}

	return jsonify({'result' : output})

@app.route('/user/<user_id>', methods = ['PUT'])
def update_user(user_id):
	if ObjectId.is_valid(user_id) == False:
		output = {'message' : 'Sorry, invalid userID'}
		return jsonify({'result' : output})
	id = ObjectId(user_id)
	data = request.get_json()
	print(data)
	name = request.json['name']
	gender = request.json['gender']
	age = request.json['age']
	status = request.json['status']
	print(name)
	user = users.update_one({'_id' : id}, {'$set': data})
	if user.modified_count != 0:
    		output = {'message' : 'Sorry, user does not exists'}
	else:
    		output = {'message' : 'User updated successfully'}
	return jsonify({'result' : output})

@app.route('/user/<user_id>', methods = ['DELETE'])
def del_user(user_id):
    	if ObjectId.is_valid(user_id) == False:
    		output = {'message' : 'Sorry, invalid userID'}
		return jsonify({'result' : output})
		id = ObjectId(user_id)
		data = request.get_json()
		
		user = users.update_one({'_id' : id}, {'$set': {'status' : False} })
		if user.modified_count != 0:
    			output = {'message' : 'Sorry, user does not exists'}
		else:
    			output = {'message' : 'User deleted successfully'}
		return jsonify({'result' : output})

@app.route('/book', methods = ['POST'])
def create_book():
	name = request.json['name']
	status = True
	book = books.insert({'name' : name, 'status' : status})
	return jsonify({'result' : 'book created successfully'})


@app.route('/book/<book_id>', methods = ['GET'])
def find_book(book_id):
	if ObjectId.is_valid(book_id) == False:
		output = {'message' : 'Sorry, invalid bookID'}
		return jsonify({'result' : output})

	id = ObjectId(book_id)
	book = books.find_one({'_id' : id})
	if book:
		print("Exists")
		output = {'name' : book['name'], 'status' : book['status'], 'id' : str(book['_id'])}
	else:
		output = {'message' : 'Sorry, book does not exists'}

	return jsonify({'result' : output})

@app.route('/book/<book_id>', methods = ['PUT'])
def update_book(book_id):
	if ObjectId.is_valid(book_id) == False:
		output = {'message' : 'Sorry, invalid bookID'}
		return jsonify({'result' : output})
	id = ObjectId(book_id)
	data = request.get_json()
	print(data)

	book = books.update_one({'_id' : id}, {'$set': data})
	if user.modified_count != 0:
    		output = {'message' : 'Sorry, book does not exists'}
	else:
    		output = {'message' : 'Book updated successfully'}
	return jsonify({'result' : output})

@app.route('/book/<book_id>', methods = ['DELETE'])
def del_book(book_id):
    	if ObjectId.is_valid(book_id) == False:
    		output = {'message' : 'Sorry, invalid bookID'}
		return jsonify({'result' : output})
		id = ObjectId(book_id)
		data = request.get_json()
		
		book = books.update_one({'_id' : id}, {'$set': {'status' : False} })
		if book.modified_count != 0:
    			output = {'message' : 'Sorry, book does not exists'}
		else:
    			output = {'message' : 'Book deleted successfully'}
		return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)

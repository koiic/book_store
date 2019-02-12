import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
# configure app
app.config.from_object(config[os.getenv('FLASK_ENV')])

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from model import Book

@app.route('/')
def main():
	return jsonify({'my_home': 'welcome home'})

@app.route('/add', methods=['POST'])
def add_book():
	""" Add a new book"""
	new_book = request.get_json()
	name = new_book.get('name')
	author = new_book.get('author')
	published = new_book.get('published')
	try:
		book = Book(
			name=name,
			author=author,
			published=published
		)
		db.session.add(book)
		db.session.commit()
		return jsonify({
			'status': 'success',
			'message': ' Book added successfully',
			'data': book

		})
	except Exception as e:
		return (str(e))

@app.route('/get')
def get_all():
	""" Fetch all books"""
	try:
		books = Book.query.all()
		return jsonify([book.serialize() for book in books])
	except Exception as e:
		return (str(e))

@app.route("/get/<id_>")
def get_book_by_id(id_):
	""" get a single book"""
	try:
		book = Book.query.filter_by(id=id_).first()
		return jsonify(book.serialize())
	except Exception as e:
		return (str(e))

@app.route("/delete/<id_>", methods=['DELETE'])
def delete_book(id_):
	""" delete a single book"""
	try:
		book = Book.query.filter_by(id=id_).first()
		if book:
			db.session.delete(book)
			db.session.commit()
		return jsonify({'status': 'success', 'message': 'book successful deleted'})
	except Exception as e:
		return (str(e))


@app.route("/update/<id_>", methods=['PATCH'])
def edit_book(id_):
	""" Update a single book"""
	updated_info = request.get_json()
	try:
		book = Book.query.filter_by(id=id_)
		# import pdb; pdb.set_trace()
		if book:
			book.update(dict(updated_info))
			# book.published = updated_info.published
			# book.name = updated_info.name
			# book.author = updated_info.author
		db.session.commit()
		return jsonify({'status': 'success', 'message': 'book successful updated'})
	except Exception as e:
		return (str(e))

if __name__ == '__main__':
	app.run()

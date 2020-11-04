import os
import uuid

import stripe
from flask import Flask, jsonify, request
from flask_cors import CORS

import json 
import book as libook

# BOOKS = []
# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True,
#         'price': '19.99'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False,
#         'price': '9.99'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True,
#         'price': '3.99'
#     }
# ]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# read books
libook.read_books()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():    
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    return libook.books(request.method, request.get_json())

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(book_id):
    return libook.book(request.method, book_id, request.get_json())

# @app.route('/charge', methods=['POST'])
# def create_charge():
#     post_data = request.get_json()
#     amount = round(float(post_data.get('book')['price']) * 100)
#     stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
#     charge = stripe.Charge.create(
#         amount=amount,
#         currency='usd',
#         card=post_data.get('token'),
#         description=post_data.get('book')['title']
#     )
#     response_object = {
#         'status': 'success',
#         'charge': charge
#     }
#     return jsonify(response_object), 200


# @app.route('/charge/<charge_id>')
# def get_charge(charge_id):
#     stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
#     response_object = {
#         'status': 'success',
#         'charge': stripe.Charge.retrieve(charge_id)
#     }
#     return jsonify(response_object), 200


if __name__ == '__main__':
    app.run()

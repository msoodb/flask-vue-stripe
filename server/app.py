import os
import uuid

import stripe_wrapper as stripe_w
from flask import Flask, jsonify, request
from flask_cors import CORS

import json 
import book

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# read books
book.read_books()

# sanity check route
@app.route('/foo', methods=['GET'])
def foo_r():    
    return jsonify('bar!')

# book route
@app.route('/books', methods=['GET', 'POST'])
def books_r():
    return book.books(request.method, request.get_json())

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_r(book_id):
    return book.book(request.method, book_id, request.get_json())

# stripe route
@app.route('/charge', methods=['POST'])
def create_charge_r():
    post_data = request.get_json()
    amount = round(float(post_data.get('book')['price']) * 100)
    currency = 'usd'
    card = post_data.get('token')
    description = post_data.get('book')['title']    
    
    return stripe_w.create_charge(amount, currency, card, description)

@app.route('/charge/<charge_id>')
def get_charge_r(charge_id):    
    return stripe_w.get_charge(charge_id)

@app.route('/checkout', methods=['POST'])
def create_checkout_session_r():    
    return stripe_w.create_checkout_session()

if __name__ == '__main__':
    app.run()

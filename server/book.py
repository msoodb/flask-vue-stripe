#import os
import uuid

#import stripe
#from flask import Flask, jsonify, request
#from flask_cors import CORS

from flask import jsonify, request
import json 

BOOKS = []
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

def read_books():
    global BOOKS
    with open('book.json') as json_file:        
        BOOKS = json.load(json_file)        
    
def __remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

def __save_books():
    json_object = json.dumps(BOOKS, indent = 4)    
    with open("book.json", "w") as outfile: 
        json.dump(BOOKS, outfile)

def __print_books():
    print(BOOKS)

def books(method, payload):
    response_object = {'status': 'success'}
    if method == 'POST':
        post_data = payload
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        __save_books()
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


def book(method, book_id, payload):
    response_object = {'status': 'success'}
    if method == 'GET':
        return_book = ''
        for book in BOOKS:
            if book['id'] == book_id:
                return_book = book
        response_object['book'] = return_book
    if method == 'PUT':
        post_data = payload
        __remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        __save_books()
        response_object['message'] = 'Book updated!'
    if method == 'DELETE':
        __remove_book(book_id)
        __save_books()
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)
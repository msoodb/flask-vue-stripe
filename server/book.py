import uuid
from flask import jsonify, request
import json 

BOOKS = []

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
from flask import Flask, jsonify, request
import mysql.connector
import json

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'books',
)

## CRUD
## comando = ''
## cursor.execute(comando)
## -> .commit(): edição do banco de dados
## -> .fetchall(): leitura do banco 

cursor = connection.cursor()

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Seu dinheiro pode mais',
        'author': 'Gerson Costa'
    },
    {
        'id': 2,
        'title': 'Meu amigo Espírito Santo',
        'author': 'PR Rodrigo Pena'
    },
    {
        'id': 3,
        'title': 'Até que nada mais importe',
        'author': 'Luciano Subirá'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    command = 'SELECT * FROM books'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    updated_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(updated_book)
            return jsonify(books[index])

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    command = f'INSERT INTO books (title, author) VALUES ("{new_book["title"]}", "{new_book["author"]}")'
    cursor.execute(command)
    connection.commit()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)

cursor.close()
connection.close()
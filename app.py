from flask import Flask, jsonify, request
import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin1',
    database = 'books',
)

cursor = connection.cursor()

cursor = connection.cursor(dictionary=True)

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    command = 'SELECT * FROM books'
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)
    return jsonify(result)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    command = f'SELECT * FROM books WHERE id = {id}'
    cursor.execute(command)
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    updated_book = request.get_json()
    command = f'UPDATE books SET author = "{updated_book["author"]}", title = "{updated_book["title"]}" WHERE id = {id}'
    cursor.execute(command)
    connection.commit()

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    command = f'INSERT INTO books (title, author) VALUES ("{new_book["title"]}", "{new_book["author"]}")'
    cursor.execute(command)
    connection.commit()
    return get_books()

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    command = f'DELETE FROM books WHERE id = {id}'
    cursor.execute(command)
    connection.commit()
    return get_books()

app.run(port=5000, host='localhost', debug=True)

cursor.close()
connection.close()
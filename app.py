from flask import Flask, jsonify, request

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
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Bíblia Sagrada',
        'author': 'Deus'
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

@app.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(books)

app.run(port=5000, host='localhost', debug=True)
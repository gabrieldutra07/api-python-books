from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Bíblia Sagrada',
        'autor': 'Deus'
    },
    {
        'id': 2,
        'título': 'Meu amigo Espírito Santo',
        'autor': 'PR Rodrigo Pena'
    },
    {
        'id': 3,
        'título': 'Até que nada mais importe',
        'autor': 'Luciano Subirá'
    }
]

@app.route('/livros')
def get_books():
    return jsonify(livros)
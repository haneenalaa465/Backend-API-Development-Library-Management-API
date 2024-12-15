from flask import Flask, jsonify, request
import json

app = Flask(__name__)

books = []

def find_book(isbn):
    for book in books:
        if book['isbn'] == isbn:
            return book
    return None

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    requested_fields = ['title', 'author', 'published_year', 'isbn']

    for field in requested_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    books.append({
        "title": data['title'],
        "author": data['author'],
        "published_year": data['published_year'],
        "isbn": data['isbn'],
        "genre": data['genre']
    })

    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({'books': books})

@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    genre = request.args.get('genre')

    results = []

    if author:
        for book in books:
            if book['author'].lower() == author.lower():
                results.append(book)
    elif published_year:
        for book in books:
            if book['published_year'] == published_year:
                results.append(book)
    elif genre:
        for book in books:
            if book['genre'].lower() == genre.lower():
                results.append(book)

    return jsonify(results), 200

@app.route('/books/<isbn>', methods=['DELETE']) 
def delete_book(isbn):
    book = find_book(isbn)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted successfully'}), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    book = find_book(isbn)
    if book:
        data = request.get_json()
        for field in data:
            book[field] = data[field]
        return jsonify({'message': 'Book updated successfully'}), 200
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
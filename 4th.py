from flask import Flask, jsonify, request
app = Flask(__name__)

# Sample data for books (for simplicity, we're using an in-memory list)
books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1'
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2'
    }
]

# GET all books
@app.route('/', methods=['GET'])
def get_books():
    return jsonify(books)

# GET a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# CREATE a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# UPDATE an existing book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json['title']
        book['author'] = request.json['author']
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# DELETE a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run()
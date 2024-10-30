from http import HTTPStatus
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request

# Simulate a database table in a list
table = [
    {'id':1, 'author':'Eric Matthes','title':'Python Crash Course', 'isbn':'978-1718502703'},
    {'id':2, 'author':'Brett Slatkin','title':'Effective Python', 'isbn':'978-0134853987'},
    {'id':3, 'author':'Luciano Ramalho','title':'Fluent Python', 'isbn':'978-1492056355'}
]

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "bart": generate_password_hash("eatmyshorts"),
    "homer": generate_password_hash("duffbeer")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    else:
        return None


@app.route('/books', methods = ['GET'])
@auth.login_required
def find_all():
    return jsonify({'data': table}), HTTPStatus.OK


@app.route('/books/<int:oid>', methods = ['GET'])
@auth.login_required
def find_by_id(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND


@app.route('/books', methods=['POST'])
@auth.login_required
def insert():
    data = request.get_json()
    print(data)
    oid = data.get('id')
    author = data.get('author')
    title = data.get('title')
    isbn = data.get('isbn')
    book = {
        'id': oid,
        'author': author,
        'title': title,
        'isbn': isbn
    }
    table.append(book)
    return jsonify(book), HTTPStatus.CREATED


@app.route('/books/<int:oid>', methods=['PUT'])
@auth.login_required
def update(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            data = request.get_json()
            print(data)
            item.update({'author':data.get('author'), 'title':data.get('title'), 'isbn':data.get('isbn')})
            return jsonify(item), HTTPStatus.OK
    return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND


@app.route('/books/<int:oid>', methods=['DELETE'])
@auth.login_required
def delete(oid):
    for item in table:
        print(item)
        if item['id'] == oid:
            table.remove(item)
            return '', HTTPStatus.NO_CONTENT
    return jsonify({'message': 'book not found'}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(port=8443, debug=True, ssl_context='adhoc')
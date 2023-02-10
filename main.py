# Flask template 
from flask import Flask, request
import words

app = Flask(__name__)

@app.route('/')
def main():
    data = words.getData('data.json')
    books = words.getBooks(data)
    books_str = ''
    # books_list = "<br>".join(books)
    for book in books:
        books_str += f'<a href="/unit?book={book}">{book}</a><br>'

    return books_str
@app.route('/unit')
def unit():
    book = request.args.get('book')
    data = words.getData('data.json')
    # print(book)
    units = data[book]
    units_str = ''
    for unit in units:
        units_str += f'<a href="/words?book={book}&unit={unit}">{unit}</a><br>'

    return units_str

@app.route('/words')
def getWords():
    book = request.args.get('book')
    unit = request.args.get('unit')
    data = words.getData('data.json')
    words_list = data[book][unit]
    words_str = ''
    for word in words_list:
        words_str += word + '<br><br>'

    return words_str

if __name__ == '__main__':
    app.run(debug=True)
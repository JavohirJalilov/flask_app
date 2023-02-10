import json

def getData(fname: str)-> dict:
    with open(fname, 'r') as f:
        data = json.loads(f.read())
    return data

def getBooks(data):
    books = data.keys()
    return list(books)
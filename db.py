from tinydb import TinyDB, Query
import json
db = TinyDB('words.json')
books = db.table('books')
# create getJson function for read json file
def getJson(fname):
    """
    This function is for read json file
    
    Args:
        fname: json file name
    Returns:
        dict: json file data
    """
    with open(fname, 'r', encoding="UTF8") as f:
        return json.load(f)

# create insertJson function for insert json file data to db
def insertJson(data):
    # print(len(data['Book 1']))
    """
    This function is for insert json file data to db
    
    Args:
        fname: json file name
    """
    books.insert(data)
    print('Insert data to db successfully')

if __name__ == '__main__':
    data = getJson('data.json')
    insertJson(data)
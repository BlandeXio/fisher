from flask import jsonify
from helper import get_isbn_or_key
from yushu_book import YuShuBook

@app.route('book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = get_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_isbn(q)
    return jsonify(result)
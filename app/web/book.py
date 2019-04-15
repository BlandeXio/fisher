from flask import jsonify, Blueprint,request
from helper import get_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book_forms import SearchForm
from . import web_bp

@web_bp.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q, page = form.q.data.strip(), form.page.data
        isbn_or_key = get_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
# date 2019/4/17


__author__ = 'Louis'

class BookViewModel:
    def __init__(self, data):
        # if not isinstance(data, dict):V
        #     author = data.author
        #     data = data.__dict__
        #     data['author'] = author
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.binding = data['binding']
        self.publisher = data['publisher']
        self.image = data['image']
        self.price = '￥' + data['price'] if data['price'] else data['price']
        self.isbn = data['isbn']
        self.pubdate = data['pubdate']
        self.summary = data['summary']
        self.pages = data['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword


class _BookViewModel:
    # 类描述特征（类变量、实例变量）
    # 行为（方法）
    # 面向过程的
    """
    1.统一结构
    2.裁剪修改数据
    """
    @classmethod
    def package_single(cls,data,keyword):
        """
        返回单本书，isbn搜索
        :param data: 原始数据,解析原始数据
        :param keyword: 关键字
        :return:
        """
        returned = {
            'books':[],
            'total':0,
            'keyword':''
        }
        if data:
            returned['total'] = 1
            returned['books'] = cls._cut_book_data(data)
        return returned

    @classmethod
    def package_collection(cls,data,keyword):
        """
        返回集合，关键字搜索
        :return:
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': ''
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def _cut_book_data(cls,data):
        """
        裁剪原始数据,单项数据的单个的处理方式，多项数据可以复用这些的数据
        :param data:原始数据
        :return:
        单页面前后端分离，可以传回列表，前端渲染也比较方便
        """
        print('data',data)
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author':'、'.join(data['author']),  # join方法，用、连接起来
            'price':data['price'],
            'summary':data['summary'] or '',
            'img':data['image'],
        }
        return book
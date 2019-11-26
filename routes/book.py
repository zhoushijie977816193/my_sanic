# !/usr/bin/python
# ! -*- coding: utf-8 -*-
# 2019.11.25


from manage import app
from logics.book.book import bookinfo_view, bookinfo_post_view


# 查询书籍信息
app.add_route(bookinfo_view, '/<source>/<version>/book/<book_id>')
# 查询书籍信息, post方法
app.add_route(bookinfo_post_view, '/<source>/<version>/book/info', methods=['POST'])

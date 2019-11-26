# !/usr/bin/python
# ! -*- coding: utf-8 -*-
# 2019.11.25


from manage import app
from logics.book.book import hello_view


# 测试接口
app.add_route(hello_view, '/<source>/<version>/test')

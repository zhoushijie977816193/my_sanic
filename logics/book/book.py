# !/usr/bin/python
# ! -*- coding: utf-8 -*-
# 2019.11.25


from sanic.response import json

from manage import session
from models.book import BookBookModels


async def hello_view(request, source, version):
    res = {"source": source, "version": version}
    res["test"] = "this is test api"
    return json(res)


async def bookinfo_view(request, source, version, book_id):
    print(request.args)
    item = session.query(BookBookModels).filter_by(id=book_id).first()
    res = item.to_json()
    return json(res)


async def bookinfo_post_view(request, source, version):
    print(request.json)
    book_id = request.json["book_id"]
    print(source, version)
    item = session.query(BookBookModels).filter_by(id=book_id).first()
    res = item.to_json()
    return json(res)

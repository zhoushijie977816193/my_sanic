# !/usr/bin/python
# ! -*- coding: utf-8 -*-
# 2019.11.25


from sanic.response import json
from sanic_openapi import doc

from manage import session
from models.book import BookBookModels


async def hello_view(request, source, version):
    user_ip = request.ip if request.ip else "127.0.0.1"
    other_para = {"source": source, "version": version, "ip": user_ip}
    res = {"test": "this is test api"}
    res = {**res, **other_para}
    return json(res)


async def bookinfo_view(request, source, version, book_id):
    user_ip = request.ip if request.ip else "127.0.0.1"
    other_para = {"source": source, "version": version, "ip": user_ip}
    item = session.query(BookBookModels).filter_by(id=book_id).first()
    res = item.to_json()
    res = {**res, **other_para}
    return json(res)


@doc.consumes({"post parameters": {"book_id": int, "chapter_id": int}}, location="body")
async def bookinfo_post_view(request, source, version):
    user_ip = request.ip if request.ip else "127.0.0.1"
    other_para = {"source": source, "version": version, "ip": user_ip}
    book_id = request.json["book_id"]
    item = session.query(BookBookModels).filter_by(id=book_id).first()
    res = item.to_json()
    res = {**res, **other_para}
    return json(res)

# /user/bin/env python3.6
# -*- coding: utf-8 -*-
# author zhoushijie 2019.11.25


from sanic import Sanic, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sanic_openapi import swagger_blueprint


from config.mysqlconfig import MySqlConfig


# database
Base = declarative_base()
engine = create_engine(
        MySqlConfig().mysql_local_url_info(),
        max_overflow=5,       # 超过连接池大小外最多创建的连接
        pool_size=20,         # 连接池大小
        pool_timeout=300,      # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1       # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
DBSession = sessionmaker(bind=engine)
session = DBSession()


# applicaption
app = Sanic()

# blueprint test
test_blueprint = Blueprint("test")
app.blueprint(test_blueprint)

# blueprinr book
book_blueprint = Blueprint("book")
app.blueprint(book_blueprint)

# app openapi
app.blueprint(swagger_blueprint)
app.config["API_TITLE"] = "Sanic-OpenAPI"
app.config["API_DESCRIPTION"] = "ZhouShiJie-Sanic-OpenAPI"
app.config["API_SCHEMES"] = ["http", "https"]
app.config["API_VERSION"] = "1.0.0"
app.config["API_BASEPATH"] = "/test"
